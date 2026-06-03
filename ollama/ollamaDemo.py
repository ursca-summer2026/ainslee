import ollama

# Set Up Ollama and its Local Models
#
# Ollama may be downloaded from https://ollama.com/. 
# The below commands will install the llama3.2 model
# that Ollama will require to perform its functions.
# Note, a typical model for Ollama is about 4 GB in
# size. There are many different models that you can
# experiment with at https://ollama.com/search.

# The following command pulls (downloads) the llama3.2
# model for use with Ollama.

# ollama pull llama3.2


# Setup virtual environment to run this code.

# python3 -m venv ./venv
# source ./venv/bin/activate
# pip install ollama
# python3 ollamaDemo.py

stream = ollama.chat(
    # model='llama3',
    model='phi3',
    # messages=[{'role': 'user', 'content': 'Explain quantum physics.'}],
    messages=[{'role': 'user', 'content': 'Explain what Apple Corporation does.'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)


