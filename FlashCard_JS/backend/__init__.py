from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from FlashCard_JS.backend.cards import Cards, Base


PROJECT_ROOT = Path(__file__).parent.parent.parent
DB = (PROJECT_ROOT / 'data' / 'deck.db').resolve()

engine = create_engine(f'sqlite:///{DB}', echo = True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)

session = Session()