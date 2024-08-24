import ast
from pathlib import Path
import requests

import pandas as pd 
from flask import Flask, request
from flask_cors import CORS

PROJECT_ROOT = Path(__file__).parent.parent.parent
DB = (PROJECT_ROOT / 'data' / 'words.csv').resolve()

app = Flask(__name__)
CORS(app)

def deck():
	return pd.read_csv(DB) 

@app.route('/load_deck', methods=['GET'])
def load_deck():
	return deck().to_json(orient='records')

@app.route('/generate', methods=['POST'])
def generate():
	userInput = request.json.get('userInput')
	URL = 'http://localhost:11434/api/generate'
	n = userInput.get('amount')
	topic = userInput.get('topic')
	languageA = userInput.get('languageA')
	languageB = userInput.get('languageB')
	question = f"Please provide {n} words related to {topic} in {languageA} and {languageB}. "
	request_format = f"Format: [{{'{languageA}': value, '{languageB}': value}}...]. "
	details = "Provide only the list"

	d = {
	  "model": "gemma2",
	  "prompt": question + request_format + details,
	  "stream": False
	}

	data = requests.post(URL, json=d)
	response = data.json().get('response')
	new_cards = pd.DataFrame(ast.literal_eval(response))
	new_cards = new_cards.rename(columns={languageA: 'question', languageB: 'answer'})
	new_cards[['topic', 'last', 'image']] = [topic, '2024-01-01', '']
	updatedDeck = pd.concat([deck(), new_cards])
	updatedDeck = updatedDeck[~updatedDeck[['topic', 'question', 'answer']].duplicated()].reset_index(drop=True)
	updatedDeck.to_csv(DB, index=False)

	return deck().to_json(orient='records')

if __name__ == '__main__':
	app.run(debug=True,  port='5003')