from pathlib import Path
import pandas as pd 
from flask import Flask, request
from flask_cors import CORS


PROJECT_ROOT = Path(__file__).parent.parent.parent
data = (PROJECT_ROOT / 'data' / 'words.csv').resolve()

app = Flask(__name__)
CORS(app)

def deck():
	return pd.read_csv(data) 

@app.route('/load_deck', methods=['GET'])
def load_deck():
	return deck().to_json(orient='records')

@app.route('/add_card', methods=['POST'])
def add():
	card = request.json.get('card')
	print(card)
	newCard = pd.DataFrame([card])

	updatedDeck = pd.concat([deck(), newCard])
	updatedDeck = updatedDeck[~updatedDeck.duplicated()]
	# updatedDeck.to_csv(data, index=False)
	
	return deck().to_json(orient='records')

if __name__ == '__main__':
	app.run(debug=True,  port='5003')