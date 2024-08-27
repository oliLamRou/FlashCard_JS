import ast

from flask import request
from flask_restful import Resource, reqparse

from FlashCard_JS.backend import session
from FlashCard_JS.backend.cards import Cards

class Deck(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('card')

    def get(self):
        cards = [{
            'id': card.id,
            'topic': card.topic,
            'question': card.question,
            'answer': card.answer,
            'score': card.score,
            'last' : card.last,
        } for card in session.query(Cards).all()]
        return cards

    def put(self):
        args = self.parser.parse_args()
        card = ast.literal_eval(args.get('card'))
        session.query(Cards).filter(Cards.id == card['id']).update({Cards.score: card['score']}, synchronize_session = False)
        session.commit()
        return self.get()
