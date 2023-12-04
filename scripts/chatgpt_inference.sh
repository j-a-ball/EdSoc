#!bin/bash

# Sociology of Education
# python chatgpt_inference.py

# American Journal of Education
python chatgpt_inference.py \
--model_name "gpt-3.5-turbo" \
--input_file data/eric/aje.json \
--completion_dir completions/AJE/chatgpt/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 

# American Educational Research Journal
python chatgpt_inference.py \
--model_name "gpt-3.5-turbo" \
--input_file data/eric/aerj.json \
--completion_dir completions/AERJ/chatgpt/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 

# American Sociological Review
python chatgpt_inference.py \
--model_name "gpt-3.5-turbo" \
--input_file data/eric/asr.json \
--completion_dir completions/ASR/chatgpt/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 

# American Journal of Sociology
python chatgpt_inference.py \
--model_name "gpt-3.5-turbo" \
--input_file data/eric/ajs.json \
--completion_dir completions/AJS/chatgpt/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 

# British Journal of Sociology of Education
python chatgpt_inference.py \
--model_name "gpt-3.5-turbo" \
--input_file data/eric/bjse.json \
--completion_dir completions/BJSE/chatgpt/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 

# International Studies in Sociology of Education
python chatgpt_inference.py \
--model_name "gpt-3.5-turbo" \
--input_file data/eric/isse.json \
--completion_dir completions/ISSE/chatgpt/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 

# random baseline
python chatgpt_inference.py \
--model_name "gpt-3.5-turbo" \
--input_file data/eric/random.json \
--completion_dir completions/random/chatgpt/fiveshot \
--template_dir prompts \
--template_file fewshot.prompt \
--n_examples 5 
