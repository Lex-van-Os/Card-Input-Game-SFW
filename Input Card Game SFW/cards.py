import random

# File for the list of cards. The file consists of at least two lists,
# list(s) of black cards (Cards with blank spots that will have to be filled) and white cards (The cards used to fill the blank spots)

main_white_cards = (
    "Corona", "Snelle op de reünie",
    "Willy", "Kabouter Wesley", "Het Vmbo",
    "Kindermeppers", "Soldaat van Oranje die niet verlengt wordt",
    "Korte vingers" "Mijn Gogo collectie", "Maandag met Lubach",
    "Geertje", "Gewoon patat majonais", "Oorsmeer", "Gordon", "Even Apeldoorn bellen", "Het juiste doen",
    "God", "Dennis Schouten", "Heel, heel, heel erg hard lachen",
    "Monica Geuze", "Ilse DeKorte", "Druif op een fuif", "Videoland",
    "Rutte is stom", "Fristibeer", "Croma bakvet", "Het Albert Heijn ouderen boodschappenuurtje",
    "Desinfecterende gel opdrinken",
    "Politievlogger Jan-Willem", "Hamburgers met korting",
    "Grapperhaus als Eggman", "Specerijen", "Samson en Gert", "Een bananendoos")

main_black_cards = ("Nieuw op RTL 4: __________",
                    "Wat verbergen mijn ouders voor me?",
                    "Hier in mijn huis gebeurt __________ niet",
                    "Maandag wasdag, woensdag gehaktdag, vrijdag ________dag", "Wat eten we vandaag?",
                    "Want Ik heb vanavond geen gemakkelijke boodschap voor u: _____________", "En hij zei: _________",
                    "________ hé, beter als 020!", "Broodje _______, komt op de TV.",
                    "Laten we toosten op ________", "Hoe kwam het dat mijn vorige relatie uit ging?",
                    "Er ontstond een oproer nadat Johan Derksen een grap maakte over _________",
                    "Yo, Ik ben _________ en vandaag gaan we _________", "Let op, geld lenen kost ________",
                    "______ & Chill", "Ernst, Bobbie en ________", "Gertje, wat doe je nou?",
                    "Ik moet je iets vertellen", "Wat wordt beter met de jaren?",
                    "In plaats van de roe, geeft Sinterklaas nu ____________ aan kinderen",
                    "Wat is mijn geheime kracht?", "Service voor een _________", "Ik hou van ______",
                    "Nieuw in ons assortiment: _________", "Nieuw van Mora: ___________!"
                    )
