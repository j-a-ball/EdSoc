__author__ = "Jon Ball"
__version__ = "October 2023"


from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import Chroma
import chromadb
import jinja2
from tqdm import tqdm
import subprocess
import argparse
import json
import os


def main(args):

    #
    model_name = "BAAI/bge-large-en"
    model_kwargs = {"device": "cpu"}
    encode_kwargs = {"normalize_embeddings": True}
    embedding_function = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
        )
    #
    persistent_client = chromadb.PersistentClient(path="chroma")
    #
    manualDB = Chroma(
        client=persistent_client,
        collection_name="manual",
        embedding_function=embedding_function,
        )
    #
    gpt4DB = Chroma(
        client=persistent_client,
        collection_name="gpt4",
        embedding_function=embedding_function,
        )
    #
    jinjitsu = jinjaLoader(args.template_dir, args.template_file)
    #
    # load records
    with open(args.input_file, "r") as infile:
        resp = json.load(infile)
    records = resp["response"]["docs"]
    #
    N_PREDICT = "80" # 80-token outputs allow for e.g. small spacing errors before cutoff
    CTX_LEN = "2987" # max([len(tokenizer.tokenize(p) for p in prompts])]) + N_PREDICT
    # randomness setting
    TEMP = "0.0"
    # loop over records
    for rec in tqdm(records[648:]):
        input3 = str(rec)
        # Pull most similar manually labeled doc
        sim1 = manualDB.similarity_search(input3, 1)[0]
        # Pull most similar gpt4 labeled doc
        sim2 = gpt4DB.similarity_search(input3, 1)[0]
        # Load the vars
        templateVars = {
            "input1": sim1.metadata["input"], "output1": sim1.metadata["output"], 
            "input2": sim2.metadata["input"], "output2": sim2.metadata["output"], 
            "input3": input3, "output3": ""
            }
        PROMPT = jinjitsu.render(templateVars)
        # Get CodeLLaMA compeletion
        completion = subprocess.run(
            ["../codellama/llama.cpp/main", 
             "-m", "../codellama/llama.cpp/models/7B/code-base-Q5_K.bin", 
             "-c", CTX_LEN,
             "-n", N_PREDICT,
             "-t", TEMP,
             "--multiline_input", 
             "-p", PROMPT], capture_output=True)
        try:
            completion = completion.stdout.decode("utf-8")
        except UnicodeDecodeError:
            completion = completion.stdout.decode("utf-8", "ignore")
        # Get only the completion following the prompt
        completion = completion.replace(PROMPT, "")
        # Save json
        templateVars["output3"] = completion
        with open(os.path.join(args.completion_dir, rec["id"] + ".json"), "w") as outfile:
            json.dump(templateVars, outfile)
    

class jinjaLoader():
    # jinja2 template renderer
    def __init__(self, template_dir, template_file):
        self.templateLoader = jinja2.FileSystemLoader(searchpath=template_dir)
        self.templateEnv = jinja2.Environment( loader=self.templateLoader )
        self.template = self.templateEnv.get_template( template_file )

    def render(self, templateVars):
        return self.template.render( templateVars )


if __name__ == "__main__":
    # args
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, default="data/eric/se.json")
    parser.add_argument("--completion_dir", type=str, default="completions/SE/7B_Q5/3shot")
    parser.add_argument("--template_dir", type=str, default="prompts")
    parser.add_argument("--template_file", type=str, default="3shot.jinja")
    args = parser.parse_args()
    # run
    main(args)
