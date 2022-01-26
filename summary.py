import os
import openai

import json


def get_keys(path):
    with open(path) as f:
        return json.load(f)


keys = get_keys("./.secret/key.json")
API_KEY = keys['API_Key']

openai.api_key = API_KEY
phrase = "D'ouest en est, son territoire s'étend de la mer Baltique (exclave de Kaliningrad) au détroit de Behring (district autonome de Tchoukotka) sur plus de 6 600 kilomètres, avec une superficie de 17 125 191 km2, soit 11,5 % des terres émergées. Limitrophe de l'Océan Arctique au nord, la Russie est caractérisée par un climat continental avec des hivers particulièrement froids et hostiles sur une grande partie du territoire, notamment en Sibérie, à l'est de l'Oural. La population russe est estimée à près de 146 millions d'habitants en 20211 ce qui en fait le neuvième pays le plus peuplé de la planète. 78 % de ses habitants vivent en Europe."

response = openai.Completion.create(
    engine="text-davinci-001",
    prompt=f"Summarize this for a second-grade student:\n\n{phrase}",
    temperature=0.7,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response.choices[0].text)
