# Ollama Project Template

Welcome to the **Ollama Project Template**! This repository provides a ready-to-use template for setting up a development environment with GitHub Codespaces or Visual Studio Code Dev Containers. The template includes the installation of Ollama and other essential dependencies to kickstart your Python effortlessly.

## Overview

This project is designed to streamline the setup process by using a `devcontainer.json` configuration file. The setup includes the following key components:

- **GitHub Dev Container**: Automatically configure a development environment with the necessary tools and dependencies.
- **Ollama Installation**: Using a custom script, the environment installs Ollama, starts its server, and prepares it for immediate use.
- **Dependency Management**: Python dependencies are handled via `pip` using the `requirements.txt` file.


## Starting the server
Before start using ollama we need to start the serever and pull a model from the library.
Here we also pull a embedding model to get embeddings from text.

bash
 ```
 ollama serve
 ollama pull gemma:2b
 ollama pull llama3.1
 ollama pull nomic-embed-text
 ```

Run chroma db
chroma run --host localhost --port 8000 --path ../vectordb-stores/chromadbchroma run --host localhost --port 8000 --path ../vectordb-stores/chromadb


# Test in Python
You can test the 
bash
 ```
python test.py -m llama3.1
 ```