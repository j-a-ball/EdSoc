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
    jinjaLoader = jinjitsu(args.template_dir, args.template_file, exampleVars)
    # load filepaths to loop over
    for dirpath, dirnames, filenames in os.walk(args.input_dir):
        files = sorted([file for file in filenames if file.endswith(".txt")])
    # Generate completions for each article
    pgnum = 2
    ctx_len = 2610 # 2610 for JES pgnum=2  3324 for SE pgnum=2
    completions = []
    for file in tqdm(files):
        with open(os.path.join(args.input_dir, file), "r") as infile:
            pgs = infile.read().split("<newpage>")
        # Render template with first n pages and output blank
        templateVars = {"input": "\n".join(pgs[:pgnum]), "output": ""}
        prompt = "\n".join([jinjaLoader.example, jinjaLoader.render( templateVars )])
        # Get GPT-4 completion and overwrite output
        completion = subprocess.run(["../codellama/llama.cpp/main", "-m", "../codellama/llama.cpp/models/7B/code-base-Q5_K.bin", "-c", ctx_len, "-n", "80", "-t", "0", "--multiline_input", "-p", prompt], capture_output=True)
        completion = completion.stdout.decode("utf-8")
        # Get only the completion following the prompt
        completion = completion.replace(prompt, "")
        # Save json
        templateVars["output"] = completion
        with open(os.path.join(args.completion_dir, file[:-4]+".json"), "w") as outfile:
            json.dump(templateVars, outfile)
        # Save txt
        completions.append(completion)
    with open(os.path.join(args.completion_dir, "responses.txt"), "w") as outfile:
        outfile.write("<sep>".join(completions))
    

class jinjitsu():
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
    parser.add_argument("--input_dir", type=str, default="data/txts/SE")
    parser.add_argument("--completion_dir", type=str, default="completions/SE/7B_Q5")
    parser.add_argument("--template_dir", type=str, default="prompts")
    parser.add_argument("--template_file", type=str, default="txt.jinja")
    parser.add_argument("--example_vars", type=str, default="prompts/examples/txt_example.json")
    args = parser.parse_args()
    # run
    main(args)
