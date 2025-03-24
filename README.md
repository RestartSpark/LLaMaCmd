# LlamaCmd
A command-line helper powered by ollama. Describe the command you need and it suggests a command

## Features
-Suggests commands based on the given description
-offline access with LLaMa setup
-command explantions
-change model via config file (model_config.txt)

## Requirements
-python 3.x
-Ollama
-ollama python library 
- any ollama model

## Setup
1. Install Ollama: See [ollama.ai](https://ollama.ai/).
2. Start Ollama: `ollama serve`.
3. Install Python library: `pip install ollama`.
4. Download a model: `ollama pull llama3`.
5. (Optional) Set model in `model.txt` (e.g., `llama3:latest`), defaults to `llama3` if absent.
6. Run: `python LLaMaCmd.py`
