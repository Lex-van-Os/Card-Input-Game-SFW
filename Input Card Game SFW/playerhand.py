import random, gamesetup


# from player import Player
# The playerhand is the hand of white cards a player has.
# Every player has a hand that consists out of cards randomly picked out of the chosen packs, these are then shuffled
# When playing a card, a card will be removed and added to the hand

class PlayerHand():

    def __init__(self, deck):
        self.deck = deck
        self.hand = self.create_hand()

    def create_hand(self):
        new_hand = []
        looped_items = []
        rand_ints = [random.randint(0, len(self.deck))-1 for x in range(10)]

        if len(gamesetup.player_obj_list) == 0:
            for x in rand_ints:
                if rand_ints.count(x) == 1:
                    pass
                elif rand_ints.count(x) > 1:
                    old_val = x
                    loop = True
                    for y in range(len(self.deck)):
                        while loop is True:
                            new_val = self.deck.index(random.choice(self.deck))
                            if rand_ints.count(new_val) > 1:
                                continue
                            else:
                                for z in range(len(rand_ints)):
                                    if rand_ints[z] == old_val:
                                        rand_ints[z] = new_val
                                        loop = False
                                        break
                                    else:
                                        pass

            for x in rand_ints:
                new_hand.append(self.deck[x])
            return new_hand

        elif len(gamesetup.player_obj_list) > 0:
            for x in rand_ints:
                for y in range(len(gamesetup.player_obj_list)):
                    for item in gamesetup.player_obj_list[y].hand:
                        looped_items.append(item)
                if rand_ints.count(x) == 1 and self.deck[x] not in looped_items:
                    pass
                elif rand_ints.count(x) > 1 or self.deck[x] in looped_items:
                    old_val = x
                    loop = True
                    for y in range(len(self.deck)):
                        while loop is True:
                            new_val = self.deck.index(random.choice(self.deck))
                            if self.deck[new_val] in looped_items or rand_ints.count(new_val) > 0:
                                continue
                            else:
                                for z in range(len(rand_ints)):
                                    if rand_ints[z] == old_val:
                                        rand_ints[z] = new_val
                                        loop = False
                                        break
                                    else:
                                        pass

            for x in rand_ints:
                new_hand.append(self.deck[x])
            return new_hand
