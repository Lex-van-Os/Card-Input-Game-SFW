import packs, random, gamesetup
from whitecarddeck import WhiteCardDeck
from playerhand import PlayerHand

# The player class for the game. Included in the player class are a white card deck and a player hand
# Both these instances are retrieved out of the whitecarddeck class.
# Included in the player class are mostly functions used for printing out information or cards

class Player():

    def __init__(self, player, name):
        self.white_card_deck = WhiteCardDeck(gamesetup.chosen_packs).white_cards
        self.player = player
        self.points = 0
        self.name = str(name)
        self.deck = self.create_deck()
        self.hand = PlayerHand(self.deck).hand
        self.card_czar = False
        self.playing_card = None
        self.won = False

    def create_deck(self):
        deck = self.white_card_deck
        random.shuffle(deck)
        self.deck = deck
        return self.deck

    def add_new_card_hand(self, picked_card):
        self.hand.pop(picked_card)
        looped_items = []
        loop = True
        for y in range(len(gamesetup.player_obj_list)):
            for item in gamesetup.player_obj_list[y].hand:
                looped_items.append(item)
        while loop:
            new_card = random.choice(self.deck)
            if new_card in looped_items:
                pass
            elif new_card not in looped_items:
                self.hand.append(new_card)
                break

    def append_played_card(self, picked_card):
        self.playing_card = self.hand[picked_card]

    def print_name(self):
        print(f"Ik ben {self.name}")

    def add_point(self):
        self.points = self.points + 1

    def choose_czar(self):
        self.card_czar = True

    def remove_czar(self):
        self.card_czar = False

    def append_czar(self, card_czar):
        gamesetup.card_czar_list.append(card_czar)

    def print_hand(self):
        print("\nSpeler " + self.name + "'s hand: ")
        print("-----------------------------------------------------------------------------------------")
        for i in range(len(self.hand)):
            print("Kaart " + str(i + 1) + ": " + self.hand[i])

    def play_card(self):
        picked_card = int(input(
            "Welke kaart wilt u spelen? Kies een nummer dat overeen komt met de positie van de kaart in de lijst: "))
        self.append_played_card(picked_card - 1)
        self.add_new_card_hand(picked_card - 1)

    def next_czar(self, player):
        gamesetup.player_obj_list[player].card_czar = False
        gamesetup.player_obj_list[player + 1].card_czar = True

    def __str__(self):
        return f"Naam: {self.name}, aantal punten: {self.points}"
