from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from FlashCard_JS.backend.deck import Deck
from FlashCard_JS.backend.generate import Generate

app = Flask(__name__)
CORS(app)

api = Api(app)
api.add_resource(Deck, '/', '/score')
api.add_resource(Generate, '/generate')

app.run(debug=True,  port='5003')