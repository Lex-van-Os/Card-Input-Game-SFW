# from . import cards
import player, packs, gamesetup, random, blackcarddeck, keyboard, re

start = False
playing = True
points = []
global card_czar

# The gameboard is where most of the functionality will be called, it is basically the menu.
# The game is started by launching gameboard, this will firstly call gamesetup to setup the game
# After calling gamesetup, gameboard will call other functions like player and playerhand

while start == False:
    new_game = input(
        'Welkom bij Kaarten Tegen de Mensheid! Wilt u een potje spelen? Antwoord met "ja" of "nee". '
        'Typ "regels" als u de regels van het spel wilt weten. ')

    if new_game[0].lower() == "j":
        start = True
        print("SETUP")
        print("-----------------------------------------------------------------------------------------")
        # Calling gamesetup for setting up the game
        gamesetup.ask_packs()
        max_points = gamesetup.ask_max_points()
        total_players = gamesetup.ask_total_players()
        gamesetup.confirm_setup(total_players, max_points)

        print("GAME")
        print("-----------------------------------------------------------------------------------------")

        for num in range(max_points):
            print("begin loop")
            if num == max_points:
                break
            else:
                shuffled_black_cards = blackcarddeck.BlackCardDeck(gamesetup.chosen_packs)
                shuffled_black_cards.create_black_deck()
                print("BLACK CARD:")
                print("-----------------------------------------------------------------------------------------")
                shuffled_black_cards.print_black_card()
                shuffled_black_cards.pop_card()

                print("czar kiezen...")
                # Function for chosing the czar, the czar is the player who doesn't play, but gets to choose the best card
                # A czar is randomly chosen, once the round is over, the next in the list will be the czar
                for x in range(len(gamesetup.player_obj_list)):
                    print(gamesetup.player_obj_list[x])
                    if gamesetup.player_obj_list[x].card_czar is True:
                        print("Czar")
                        print(gamesetup.player_obj_list[x].player)
                        print(len(gamesetup.player_obj_list))
                        gamesetup.player_obj_list[x].remove_czar()
                        if gamesetup.player_obj_list[x].player == len(gamesetup.player_obj_list):
                            card_czar = gamesetup.player_obj_list[0]
                        else:
                            card_czar = gamesetup.player_obj_list[x + 1]
                        card_czar.choose_czar()
                        print("End of czar")
                        break
                    else:
                        if num > 0:
                            continue
                        else:
                            print("czar nog niet gekozen")
                            card_czar = random.choice(gamesetup.player_obj_list)
                            card_czar.choose_czar()
                            card_czar.append_czar(card_czar)
                            break

                print("KAART TSAAR:")
                print("-----------------------------------------------------------------------------------------")
                print(card_czar)
                print('\n')

                for x in range(len(gamesetup.player_obj_list)):
                    if not gamesetup.player_obj_list[x].card_czar:
                        gamesetup.player_obj_list[x].print_hand()
                        gamesetup.player_obj_list[x].play_card()
                    else:
                        continue
                print("\n \nGESPEELDE KAARTEN:")
                print("-----------------------------------------------------------------------------------------")
                # Printing the played cards
                for x in range(len(gamesetup.player_obj_list)):
                    if not gamesetup.player_obj_list[x].card_czar:
                        shuffled_black_cards.play_black_card(x)
                    else:
                        continue
                for x in range(len(gamesetup.player_obj_list)):
                    if gamesetup.player_obj_list[x].card_czar:
                        chosen_card_name = input(
                            "\nSelecteer de beste kaart, doe dit door de naam van de speler mee te geven: ")
                        print("\n \nSCOREBORD:")
                        print("-----------------------------------------------------------------------------------------")
                        for x in range(len(gamesetup.player_obj_list)):
                            if not gamesetup.player_obj_list[x].card_czar:
                                if chosen_card_name == gamesetup.player_obj_list[x].name:
                                    gamesetup.player_obj_list[x].add_point()
                            print(gamesetup.player_obj_list[x])

        # This and the for loop under it, are used for calculating who has the most points and who won
        for x in range(len(gamesetup.player_obj_list)):
            points.append(gamesetup.player_obj_list[x].points)
        points.sort()
        winner_names = []

        highest_score = points[-1]
        for x in range(len(gamesetup.player_obj_list)):
            if gamesetup.player_obj_list[x].points == highest_score and points.count(highest_score) == 1:
                print("\nDe winnaar is: {}!".format(gamesetup.player_obj_list[x].name))
            elif gamesetup.player_obj_list[x].points == highest_score and points.count(highest_score) > 1:
                winner_names.append(gamesetup.player_obj_list[x].name)
            else:
                pass

        if len(winner_names) > 0:
            winners = " en ".join(winner_names)
            print("\nGelijkspeltussen: {}!".format(winners))


        # Asking the user if he wants to start another game
        breakNewGame = False
        while not breakNewGame:
            new_game = input('Wilt u nog een potje spelen? Antwoord met "ja" of "nee"')
            if new_game[0].lower() == 'j':
                breakNewGame = True
                start = False

            elif new_game[0].lower() == 'n':
                breakNewGame = True
                print("Fijne dag!")

            else:
                print("Geen geldige invoer")
                continue



    elif new_game[0].lower() == "n":
        print("Fijne dag!")

    elif new_game[0].lower() == "r":
        gamesetup.rules()

    else:
        print("Geen geldige invoer")