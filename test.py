import argparse
import requests
import sys
from ollama import Client

def check_server_status(url='http://localhost:11434'):
    """Check if the Ollama server is up and running."""
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def check_model_available(client, model_name):
    """Check if the specified model is available."""
    models_info = client.list()
    models = models_info.get('models', [])
    return any(model['name'].startswith(model_name) for model in models)

def generate_with_model(model_name):
    """Generate a response from the specified model."""
    client = Client(host='http://localhost:11434')

    if not check_model_available(client, model_name):
        print(f"Error: Model '{model_name}' not found. Ensure it is pulled and available.")
        sys.exit(1)

    response = client.generate(
        model=model_name,
        prompt="Introduce yourself in a maximum of 25 words."
    )

    print(f"Response from {model_name}: ")
    print(response['response'])

def main():
    parser = argparse.ArgumentParser(description="Test Ollama model.")
    parser.add_argument('-m', '--model', required=True, help="The model name to use (e.g., llama3.1).")
    args = parser.parse_args()

    if not check_server_status():
        print("Error: Ollama server is not running. Please start the server and try again.")
        sys.exit(1)
    
    print("Ollama server is running and ready to accept requests.")

    generate_with_model(args.model)

if __name__ == "__main__":
    main()