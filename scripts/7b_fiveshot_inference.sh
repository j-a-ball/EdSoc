#!bin/bash

# Sociology of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/se.json \
--completion_dir completions/SE/7B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 4575 \
--temp 0.0 \
--threads 8

# American Journal of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/aje.json \
--completion_dir completions/AJE/7B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 4330 \
--temp 0.0 \
--threads 8

# American Educational Research Journal
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/aerj.json \
--completion_dir completions/AERJ/7B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 4312 \
--temp 0.0 \
--threads 8

# American Sociological Review
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/asr.json \
--completion_dir completions/ASR/7B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 4418 \
--temp 0.0 \
--threads 8

# American Journal of Sociology
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/ajs.json \
--completion_dir completions/AJS/7B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 3909 \
--temp 0.0 \
--threads 8

# British Journal of Sociology of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/bjse.json \
--completion_dir completions/BJSE/7B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 4440 \
--temp 0.0 \
--threads 8

# International Studies in Sociology of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/isse.json \
--completion_dir completions/ISSE/7B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 4262 \
--temp 0.0 \
--threads 8

# random baseline
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/random.json \
--completion_dir completions/random/7B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 4220 \
--temp 0.0 \
--threads 8
