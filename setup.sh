#!/bin/bash

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama serve
ollama serve

# Pull llama3.1 model
ollama pull llama3.1

# Print custom message and list installed models
ollama list

# Python test
python test.py