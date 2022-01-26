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

response = openai.Completion.create(
  engine="text-davinci-001",
  prompt="Extract keywords from this text:\n\nIl occupe d'abord les fonctions de maire de Neuilly-sur-Seine, député, ministre du Budget et porte-parole du gouvernement ou encore de président par intérim du Rassemblement pour la République (RPR).",
  temperature=0.3,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0.8,
  presence_penalty=0
)

print(response.choices[0].text)