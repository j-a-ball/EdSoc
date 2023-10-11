from tqdm import tqdm
import jinja2
import json
import subprocess
import argparse
import os

class jinjitsu():
    def __init__(self, template_dir, template_file, exampleVars):
        self.templateLoader = jinja2.FileSystemLoader(searchpath=template_dir)
        self.templateEnv = jinja2.Environment( loader=self.templateLoader )
        self.template = self.templateEnv.get_template( template_file )
        self.example = self.template.render( exampleVars )

    def render(self, templateVars):
        return self.template.render( templateVars )

def main(args):
    # inputs are .txt, outputs are .json {"input":str, "output":str}
    # load an initial one-shot example
    with open(args.example_json, "r") as infile:
        exampleVars = json.load(infile)
    # jinja templates
    jinjitsu = jinjitsu(args.template_dir, args.template_file, exampleVars)
    # load filepaths to loop over
    for dirpath, dirnames, filenames in os.walk(args.txt_dir):
        files = [file for file in filenames if file.endswith(".txt")]
    # Generate completions for each article
    completions = []
    for file in tqdm(files):
        with open(os.path.join(args.txt_dir, file), "r") as infile:
            pgs = infile.read().split("<newpage>")
        # Render template with output blank
        templateVars = {
            "input": """
            <newpage json_schema={"quantitative": bool, "qualitative": bool, "primary/secondary": bool, "tertiary": bool, "inequality": bool, "nonstructural": bool, "culture": bool, "school": bool, "state": bool, "labor": bool, "comparative": bool, "methods": bool}>
            """.join(pgs[:3]),
            "output": ""}
        prompt = "\n".join(
            [jinjitsu.example, jinjitsu.render( templateVars )])
        # Get GPT-4 completion and overwrite output
        completion = subprocess.run(["../codellama/llama.cpp/main", "-m", "../codellama/llama.cpp/models/7B/code-base-Q5_K.bin", "-c", "8000", "-n", "80", "--multiline_input", "-p", prompt], capture_output=True)
        completion = completion.stdout.decode("utf-8")
        templateVars["output"] = completion[len(prompt):]
        # Save json
        with open(os.path.join(args.completion_dir, file[:-4]+".json"), "w") as outfile:
            json.dump(templateVars, outfile)
        completions.append(completion)
    with open(os.path.join(args.completion_dir, "responses.txt"), "w") as outfile:
        outfile.write("<sep>".join(completions))

if __name__ == "__main__":
    # args
    parser = argparse.ArgumentParser()
    parser.add_argument("--txt_dir", type=str, default="data/txts/SE")
    parser.add_argument("--completion_dir", type=str, default="completions/SE")
    parser.add_argument("--template_dir", type=str, default="prompts")
    parser.add_argument("--template_jinja", type=str, default="txt.jinja")
    parser.add_argument("--example_json", type=str, default="prompts/examples/txt_example.json")
    args = parser.parse_args()
    # run
    main(args)
