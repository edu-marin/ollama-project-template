import requests
import time

# Check if the Ollama server is up and running
def check_server_status(url='http://localhost:11434'):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

# Wait for the server to be ready
def wait_for_server():
    print("Waiting for the Ollama server to start...")
    while not check_server_status():
        print("Ollama server not ready yet. Retrying in 5 seconds...")
        time.sleep(5)
    print("Ollama server is up and running!")

# Function to interact with the model
def chat_with_model():
    from ollama import Client
    
    client = Client(host='http://localhost:11434')
    
    response = client.generate(
        model='llama3.1', 
        prompt='Introduce yourself in 25 words'
    )
    
    print("Response from Llama 3.1 model:")
    print(response['response'])

if __name__ == "__main__":
    wait_for_server()
    chat_with_model()