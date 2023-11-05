#!bin/bash

# Sociology of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/se.json \
--completion_dir completions/SE/7B_Q5/oneshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 1 \
--n_predict 75 \
--ctx_len 2006 \
--temp 0.0

# American Journal of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/aje.json \
--completion_dir completions/AJE/7B_Q5/oneshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 1 \
--n_predict 75 \
--ctx_len 2001 \
--temp 0.0

# American Educational Research Journal
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/aerj.json \
--completion_dir completions/AERJ/7B_Q5/oneshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 1 \
--n_predict 75 \
--ctx_len 1988 \
--temp 0.0

# American Sociological Review
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/asr.json \
--completion_dir completions/ASR/7B_Q5/oneshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 1 \
--n_predict 75 \
--ctx_len 1849 \
--temp 0.0

# American Journal of Sociology
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/ajs.json \
--completion_dir completions/AJS/7B_Q5/oneshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 1 \
--n_predict 75 \
--ctx_len 1492 \
--temp 0.0

# British Journal of Sociology of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/bjse.json \
--completion_dir completions/BJSE/7B_Q5/oneshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 1 \
--n_predict 75 \
--ctx_len 2432 \
--temp 0.0

# International Studies in Sociology of Education
python fewshot_inference.py \
--model_path ../codellama/llama.cpp/models/7B/code-instruct-Q5_K.bin \
--input_file data/eric/isse.json \
--completion_dir completions/ISSE/7B_Q5/oneshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 1 \
--n_predict 75 \
--ctx_len 1947 \
--temp 0.0