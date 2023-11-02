#!bin/bash

# Sociology of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/se.json \
--completion_dir completions/SE/7B_Q5/fewshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 3 \
--n_predict 75 \
--ctx_len 2804 \
--temp 0.0

# American Journal of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/aje.json \
--completion_dir completions/AJE/7B_Q5/fewshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 3 \
--n_predict 75 \
--ctx_len 2688 \
--temp 0.0

# American Educational Research Journal
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/aerj.json \
--completion_dir completions/AERJ/7B_Q5/fewshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 3 \
--n_predict 75 \
--ctx_len 2571 \
--temp 0.0

# American Sociological Review
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/asr.json \
--completion_dir completions/ASR/7B_Q5/fewshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 3 \
--n_predict 75 \
--ctx_len 2578 \
--temp 0.0

# American Journal of Sociology
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/ajs.json \
--completion_dir completions/AJS/7B_Q5/fewshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 3 \
--n_predict 75 \
--ctx_len 2186 \
--temp 0.0

# British Journal of Sociology of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/bjse.json \
--completion_dir completions/BJSE/7B_Q5/fewshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 3 \
--n_predict 75 \
--ctx_len 2786 \
--temp 0.0

# International Studies in Sociology of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/isse.json \
--completion_dir completions/ISSE/7B_Q5/fewshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 3 \
--n_predict 75 \
--ctx_len 2477 \
--temp 0.0