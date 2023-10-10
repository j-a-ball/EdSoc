from tqdm import tqdm
import subprocess
import os

def main():
    # 
    txt_dir = "jes-txts"
    data_dir = "data/7B_Q5_JES"
    #
    for dirpath, dirnames, filenames in os.walk(txt_dir):
        dirp = dirpath
        files = [file for file in filenames if file.endswith(".txt")]
# Generate responses for each article
    responses = []
    for file in tqdm(files):
        input = ""
        with open(os.path.join(dirp, file), "r") as infile:
            pgs = infile.read().split("<newpage>")
        input = "\n".join(pgs[:3])
        prompt = p1 + input + p2
        response = subprocess.run(["../codellama/llama.cpp/main", "-m", "../codellama/llama.cpp/models/7B/code-base-Q5_K.bin", "-c", "8000", "-n", "80", "--multiline_input", "-p", prompt], capture_output=True)
        response = response.stdout.decode("utf-8")
        # Save
        with open(os.path.join(data_dir, file), "w") as outfile:
            outfile.write(response)
        responses.append(response)
    with open(os.path.join(data_dir, "responses.txt"), "w") as outfile:
        outfile.write("<newpage>".join(responses))

if __name__ == "__main__":
    main()
