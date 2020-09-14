import packs, random, re, gamesetup

# Class for the black card deck. In this function the deck of black cards that's used in the game will be created.
# Besides the functionality for creating a deck, other functions for showing the black cards and inserting the white cards are also included
# Black cards are created by retrieving them out of the pack class and shuffling them

class BlackCardDeck():

    def __init__(self, my_packs_new):
        self.my_packs_new = my_packs_new
        self.playing_black_card = None
        self.black_cards = []

    def create_black_deck(self):
        for packs in self.my_packs_new:
            black_card_list = [x for x in packs.black_cards]
            for items in black_card_list:
                self.black_cards.append(items)
        random.shuffle(self.black_cards)

    def print_black_card(self):
        self.playing_black_card = self.black_cards[0]
        print(self.black_cards[0] + '\n \n')

    def play_black_card(self, x):
        # This function is used for filling the blanks in black cards
        if '_' in self.playing_black_card:
            underscore = len(re.findall('_', self.playing_black_card)) - 1
            x_playing_black_card = self.playing_black_card.replace("_", '', underscore)
            x_playing_black_card = x_playing_black_card.replace("_", gamesetup.player_obj_list[
                x].playing_card)
            print(f"{gamesetup.player_obj_list[x].name}'s keuze: {x_playing_black_card}")
        else:
            x_playing_black_card = self.playing_black_card + " " + gamesetup.player_obj_list[x].playing_card
            print(f"{gamesetup.player_obj_list[x].name}'s keuze: {x_playing_black_card}")

    def pop_card(self):
        self.black_cards.pop(0)
