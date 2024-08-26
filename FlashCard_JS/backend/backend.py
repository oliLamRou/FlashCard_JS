import ast
from pathlib import Path
import requests

import pandas as pd 
from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Customers(Base):
    __tablename__ = 'deck'
    id = Column(Integer, primary_key = True)

    topic = Column(String)
    question = Column(String)
    answer = Column(String)
    score = Column(Integer)

engine = create_engine('sqlite:///../../data/deck.db', echo = True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()

# c1 = Customers(name = 'Ravi Kumar', address = 'Station Road Nanded', email = 'ravi@gmail.com')

# session.add(c1)
# session.commit()

class Deck(Resource):
    def __init__(self):
        self.PROJECT_ROOT = Path(__file__).parent.parent.parent
        self.DB = (self.PROJECT_ROOT / 'data' / 'words.csv').resolve()

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('userInput')

    @property
    def deck(self):
        return pd.read_csv(self.DB)

    def get(self):
        return self.deck.to_json(orient='records')

class Generate(Deck):
    def __init__(self):
        super().__init__()

    def post(self):
        args = self.parser.parse_args()
        userInput = ast.literal_eval(args.get('userInput'))
        print(userInput)
        print(type(userInput))
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
        new_cards[['topic', 'last', 'image', 'score']] = [topic, '2024-01-01', '', 0]
        updatedDeck = pd.concat([self.deck, new_cards])
        updatedDeck = updatedDeck[~updatedDeck[['topic', 'question']].duplicated()].reset_index(drop=True)
        updatedDeck.to_csv(self.DB, index=False)

        return self.deck.to_json(orient='records')

if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    api.add_resource(Deck, '/')
    api.add_resource(Generate, '/generate')
    # app.run(debug=True,  port='5003')