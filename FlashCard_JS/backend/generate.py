import ast
import requests

from FlashCard_JS.backend import session
from FlashCard_JS.backend.cards import Cards
from FlashCard_JS.backend.deck import Deck

class Generate(Deck):
    URL = 'http://localhost:11434/api/generate'

    def __init__(self):
        super().__init__()
        self.userInput = {}
        self.parser.add_argument('userInput')

    @property
    def topic(self):
        return self.userInput.get('topic')

    @property
    def languageA(self):
        return self.userInput.get('languageA')

    @property
    def languageB(self):
        return self.userInput.get('languageB')

    @property
    def amount(self):
        return self.userInput.get('amount')

    @property
    def prompt(self):
        question = f"Please provide {self.amount} words related to {self.topic} in {self.languageA} and {self.languageB}. "
        request_format = f"Format: [{{'{self.languageA}': value, '{self.languageB}': value}}...]. "
        details = "Provide only the list"
        prompt = {
          "model": "gemma2",
          "prompt": question + request_format + details,
          "stream": False
        }
        return prompt

    def add(self, response):
        for card in ast.literal_eval(response):
            c = Cards(topic = self.topic, question = card.get(self.languageA), answer = card.get(self.languageB), score = 0)
            session.add(c)

        session.commit()        

    def post(self):
        args = self.parser.parse_args()
        self.userInput = ast.literal_eval(args.get('userInput'))
        
        data = requests.post(self.URL, json=self.prompt)
        response = data.json().get('response')
        self.add(response)
        
        return self.get()

