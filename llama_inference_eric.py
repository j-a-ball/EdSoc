from tqdm import tqdm
import jinja2
import json
import subprocess
import argparse
import os

def main(args):
    # inputs are .txt, outputs are .json {"input":str, "output":str}
    # load an initial one-shot example
    with open(args.example_vars, "r") as infile:
        exampleVars = json.load(infile)
    # jinja template loader
    jinjitsu = jinjaLoader(args.template_dir, args.template_file, exampleVars)
    # load filepaths to loop over
    with open(args.input_file, "r") as infile:
        resp = json.load(infile)
    records = resp["response"]["docs"]
    # 2248 tokens is max prompt length for SE
    # AJE - 2170, AERJ - 2200, ASR - 2097, AJS - 1673, BJSE - 2644, ISSE - 2135
    # 74 is the length of a correct json output in tokens
    N_PREDICT = "80" # 80-token outputs allow for e.g. small spacing errors before cutoff
    CTX_LEN = "2216" # approx max([len(tokenizer.tokenize(p) for p in prompts])]) + N_PREDICT
    # randomness setting
    TEMP = "0.0"
    # seperator for few-shot learning
    SEP = "<sep>"
    # loop over records
    for rec in tqdm(records):
        # Render template with json record as input and output blank
        templateVars = {"input": str(rec), "output": ""}
        PROMPT = SEP.join([jinjitsu.example, jinjitsu.render(templateVars)])
        # Get GPT-4 completion and overwrite output
        completion = subprocess.run(
            ["../codellama/llama.cpp/main", 
             "-m", "../codellama/llama.cpp/models/7B/code-base-Q5_K.bin", 
             "-c", CTX_LEN,
             "-n", N_PREDICT,
             "-t", TEMP,
             "--multiline_input", 
             "-p", PROMPT], capture_output=True)
        completion = completion.stdout.decode("utf-8")
        # Get only the completion following the prompt
        completion = completion.replace(PROMPT, "")
        # Save json
        templateVars["output"] = completion
        with open(os.path.join(args.completion_dir, rec["id"] + ".json"), "w") as outfile:
            json.dump(templateVars, outfile)
    

class jinjaLoader():
    # jinja2 template renderer
    def __init__(self, template_dir, template_file, exampleVars):
        self.templateLoader = jinja2.FileSystemLoader(searchpath=template_dir)
        self.templateEnv = jinja2.Environment( loader=self.templateLoader )
        self.template = self.templateEnv.get_template( template_file )
        self.example = self.template.render( exampleVars )

    def render(self, templateVars):
        return self.template.render( templateVars )


if __name__ == "__main__":
    # args
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, default="data/eric/se.json")
    parser.add_argument("--completion_dir", type=str, default="completions/SE/7B_Q5")
    parser.add_argument("--template_dir", type=str, default="prompts")
    parser.add_argument("--template_file", type=str, default="json.jinja")
    parser.add_argument("--example_vars", type=str, default="prompts/examples/json_example.json")
    args = parser.parse_args()
    # run
    main(args)
