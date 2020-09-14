# In the pack class, a pack will be created. The pack contains a number so that each created pack will be unique
# The pack will also contain white cards and black cards, the given cards will be retrieved out of cards.py
class Pack:

    def __init__(self, number, name, description, white_cards, black_cards):
        self.number = number
        self.name = name
        self.description = description
        self.white_cards = white_cards  # Expect white_cards list from cards.py
        self.black_cards = black_cards  # Expect black_cards list from cards.py
