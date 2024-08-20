from pathlib import Path
import pandas as pd 
from flask import Flask, request
from flask_cors import CORS


PROJECT_ROOT = Path(__file__).parent.parent.parent
data = (PROJECT_ROOT / 'data' / 'words.csv').resolve()



app = Flask(__name__)
CORS(app)

@app.route('/get_words', methods=['GET'])
def pair_info():
	df = pd.read_csv(data)
	return df.to_json(orient='records')

app.run(debug=True,  port='5003')