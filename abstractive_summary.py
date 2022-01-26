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

# phrase = "Nicolas Paul Stéphane Sarközy de Nagy-Bocsa (/sɑːrˈkoʊzi/; French: [nikɔla pɔl stefan saʁkɔzi də naʒi bɔksa] (audio speaker iconlisten); born 28 January 1955) is a French politician who served as President of France from 16 May 2007 until 15 May 2012."

phrase = "Nicolas Sarközy de Nagy-Bocsae, dit Nicolas Sarkozy (/ni.kɔ.la saʁ.kɔ.zi/f ; Écouter), né le 28 janvier 1955 à Paris, est un homme d'État français. Il est président de la République française du 16 mai 2007 au 15 mai 2012."

response = openai.Completion.create(
  engine="text-davinci-001",
  prompt=f"{phrase}\n\n\nTl;dr\n",
  temperature=0.7,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].text)