__author__ = "Jon Ball"
__version__ = "October 2023"

from langchain.embeddings import SentenceTransformerEmbeddings
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
    model_name = "Muennighoff/SGPT-125M-weightedmean-nli-bitfit"
    model_kwargs = {"device": "cpu"}
    encode_kwargs = {"normalize_embeddings": True}
    embedding = SentenceTransformerEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
        )
    # Set up local chroma client
    persistent_client = chromadb.PersistentClient(path="chroma")
    # Vector db of 10 hand-labeled examples
    manualDB = Chroma(
        client=persistent_client,
        collection_name="manual",
        embedding_function=embedding,
        )
    # Vector db of 90 examples labeled by GPT-4
    gpt4DB = Chroma(
        client=persistent_client,
        collection_name="gpt4",
        embedding_function=embedding
        )
    #
    jinjitsu = jinjaLoader(args.template_dir, args.template_file)
    #
    # load records
    with open(args.input_file, "r") as infile:
        resp = json.load(infile)
    records = resp["response"]["docs"]
    # loop over records
    for rec in tqdm(records):
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
             "-m", args.model_path, 
             "-c", args.ctx_len,
             "-n", args.n_predict,
             "-t", args.temp,
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
    parser.add_argument("--model_path", type=str, default="../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin")
    parser.add_argument("--input_file", type=str, default="data/eric/se.json")
    parser.add_argument("--completion_dir", type=str, default="completions/SE/7B_Q5/fewshot")
    parser.add_argument("--template_dir", type=str, default="prompts")
    parser.add_argument("--template_file", type=str, default="fewshot.prompt")
    parser.add_argument("--n_predict", type=str, default="75")
    parser.add_argument("--ctx_len", type=str, default="2804")
    parser.add_argument("--temp", type=str, default="0.0")
    args = parser.parse_args()
    # run
    main(args)
