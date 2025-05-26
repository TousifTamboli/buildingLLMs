import certifi
import os

# Tell requests to use certifi's certs explicitly
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

import tiktoken
tokenizer = tiktoken.get_encoding("gpt2")

print("tiktoken loaded successfully!")
