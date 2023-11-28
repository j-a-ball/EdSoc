#!bin/bash

# Sociology of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/34B/codellama-34b-instruct.Q5_K_M.gguf \
--input_file data/eric/se.json \
--completion_dir completions/SE/34B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 4575 \
--temp 0.0 \
--threads 24

# American Journal of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/34B/codellama-34b-instruct.Q5_K_M.gguf \
--input_file data/eric/aje.json \
--completion_dir completions/AJE/34B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 4330 \
--temp 0.0 \
--threads 24

# American Educational Research Journal
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/34B/codellama-34b-instruct.Q5_K_M.gguf \
--input_file data/eric/aerj.json \
--completion_dir completions/AERJ/34B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 4312 \
--temp 0.0 \
--threads 24

# American Sociological Review
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/34B/codellama-34b-instruct.Q5_K_M.gguf \
--input_file data/eric/asr.json \
--completion_dir completions/ASR/34B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 4418 \
--temp 0.0 \
--threads 24

# American Journal of Sociology
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/34B/codellama-34b-instruct.Q5_K_M.gguf \
--input_file data/eric/ajs.json \
--completion_dir completions/AJS/34B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 3909 \
--temp 0.0 \
--threads 24

# British Journal of Sociology of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/34B/codellama-34b-instruct.Q5_K_M.gguf \
--input_file data/eric/bjse.json \
--completion_dir completions/BJSE/34B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 4440 \
--temp 0.0 \
--threads 24

# International Studies in Sociology of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/34B/codellama-34b-instruct.Q5_K_M.gguf \
--input_file data/eric/isse.json \
--completion_dir completions/ISSE/34B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 4262 \
--temp 0.0 \
--threads 24

# random baseline
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/34B/codellama-34b-instruct.Q5_K_M.gguf \
--input_file data/eric/random.json \
--completion_dir completions/random/34B_Q5/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 \
--n_predict 75 \
--ctx_len 4220 \
--temp 0.0 \
--threads 24
