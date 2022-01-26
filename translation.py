# basic translation example
import os
import openai

import json


def get_keys(path):
    with open(path) as f:
        return json.load(f)


keys = get_keys("./.secret/key.json")
API_KEY = keys['API_Key']

openai.api_key = API_KEY
# openai.api_key = os.getenv("OPENAI_API_KEY")

phrase = 'What rooms do you have available?'
response = openai.Completion.create(
  engine="text-davinci-001",
  prompt=f"Translate this into 1. French:\n\n{phrase}\n\n1.",
  temperature=0.3,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].text)
