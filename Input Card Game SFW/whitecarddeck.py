import packs, random


# This class is used for creating a deck for white cards.
# The white cards are retrieved out of the pack, these will then also be used to create a player hand out of a deck

class WhiteCardDeck():

    def __init__(self, chosen_packs):
        self.white_cards = []
        for packs in chosen_packs:
            white_card_list = [x for x in packs.white_cards]
            for items in white_card_list:
                self.white_cards.append(items)
