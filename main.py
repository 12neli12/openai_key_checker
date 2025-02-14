from openai import OpenAI
import requests
import os

path = "input"
output_dir = "output"
output_file = "output.txt"

def check_file(input_path):
    if not os.listdir(input_path):
        return
    file = os.listdir(path)[0]
    iterate_file(file)

def check_key(key):
    open_ai_key = key

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {open_ai_key}",
        "Content-Type": "application/json"
    }

    # Request payload
    data = {
        "model": "gpt-4o-mini",  # Specify the model
        "messages": [{"role": "user", "content": "Hello"}],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        with open(f"{output_dir}/{output_file}", "a") as file:
            print("Jackpot!")
            file.write(f"{open_ai_key}\n")
    else:
        print(f"Error: {response.status_code}")

def iterate_file(file):
    with open(f"{path}/{file}") as f:
        for line in f:
            check_key(line.strip())

check_file(path)
