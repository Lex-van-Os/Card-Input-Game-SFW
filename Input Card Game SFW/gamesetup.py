import packs, whitecarddeck, blackcarddeck, player

# The gamesetup class is used for setting up the game
# The gamesetup will ask for the packs of cards the user wants to use, max points and the amount of players

players = []
player_obj_list = []
card_czar_list = []
chosen_packs = []
shuffled_black_cards = []
test = 45

my_packs = packs.my_packs

def ask_packs():
    print("Packs:")
    for pack in my_packs:
        print("Nummer: {} | Pack naam: {}".format(pack.number, pack.name))
    print(
        "Met welke packs wilt u spelen? Typ het nummer van de pack om het toe te voegen, typ 'bevestig' om te bevestigen. ")
    break_loop = False
    while not break_loop:
        chosen_digit = input("Kies uw pack(s) uit: ")
        try:
            if chosen_digit.isdigit() and my_packs[int(chosen_digit) - 1] not in chosen_packs:
                chosen_packs.append(my_packs[int(chosen_digit) - 1])
            elif chosen_digit[0].lower() == 'b':
                return chosen_packs
            elif chosen_digit[0].lower != 'b':
                print("Voer een geldig nummer in")
            elif my_packs[int(chosen_digit) - 1] in chosen_packs:
                print("Pack is al toegevoegd!")
                continue
        except IndexError:
            print("Voer een geldig nummer in")


def ask_max_points():
    break_loop = False
    while not break_loop:
        try:
            max_points = int(input("Tot hoeveel punten wilt u spelen? "))
            return max_points
        except ValueError:
            print("Voer een geldig nummer in")
            continue


def ask_total_players():
    break_loop = False
    while not break_loop:
        try:
            total_players = int(input("Met hoeveel spelers wilt u spelen? "))
            for x in range(total_players):
                player_name = input(f"Speler {x + 1}, voer uw naam in. ")
                players.append(player)
                player_obj_list.append(player.Player(x + 1, player_name))
            return total_players
        except ValueError:
            print("Voer een geldig nummer in")
            continue

def confirm_setup(total_players, max_points):
    print(f"U wilt met {total_players} spelers spelen")
    print(f"U wilt tot {max_points} spelen")
    print("U wilt met de volgende packs spelen: ")
    for pack in chosen_packs:
        print(pack.name)
    confirm = input('Klopt deze invoer? Antwoord met "ja" of "nee" ')
    if confirm[0].lower() == 'j':
        pass
    elif confirm[0].lower() == 'n':
        ask_total_players()


def rules():
    print(
        "Het spel begint met het opzetten van het spel, vervolgens zullen de gebruikte packs met kaarten meegegeven moeten worden, het aantal spelers met de namen en het aantal punten")
    print(
        "Wanneer het spel is opgezet, begint het spel met het tonen van de eerste black card. De zin bevat een of meer lege plekken die ingevuld kunnen worden met een van de 10 white cards die elke speler in hun deck krijgt")
    print(
        "Naast de kaart zelf, zal er ook een card czar gekozen en getoond worden. De card czar speelt die ronde niet mee, inplaats van meespelen kiest de card czar wie er een punt verdient")
    print(
        "Nadat elke speler een kaart heeft gekozen, worden deze getoond en mag de card czar zijn keuze uitkiezen, diegene krijgt een punt")
    print("Dit proces zal zich herhalen gebaseerd op het aantal meegegeven punten, degene met de hoogste punten wint\n")
