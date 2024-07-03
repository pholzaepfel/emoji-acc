import requests
from gtts import gTTS
from playsound import playsound
import threading
import os

def get_chatgpt_completion(prompt, api_key):
    """
    Function to get a completion from the ChatGPT API.

    Parameters:
    prompt (str): The input text to generate a completion for.
    api_key (str): Your OpenAI API key.

    Returns:
    str: The generated completion text.
    """
    api_url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "messages": [
            {
                "role": "system",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "model": "gpt-4o"
    }

    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 200:
        completion = response.json()["choices"][0]["message"]["content"]
        return completion.strip()
    else:
        response.raise_for_status()


api_key = "YOUR_KEY_HERE"

i=0
while True:
    word = input("Insert emojis to convert: ")

    prompt = "Please convert the following string of emojis [" + word + "] into a short plausible sentence. For example, 🍺😀 might mean 'beer makes me happy'. 👀🐐😍 might mean 'look at the cute goat'. Respond only with a short sentence based on the emojis, never anything else."

    out = get_chatgpt_completion(prompt, api_key)
    print(out)
    myobj = gTTS(text = out, lang = 'en', slow = False)

    myobj.save(str(i) + ".mp3")
    playsound(str(i) + ".mp3")
    i+=1
