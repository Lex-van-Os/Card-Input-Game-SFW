import random
import pack
import cards

# In this class, the existing packs are created. If the pack is added to my_packs, the pack will be
# Shown under the available packs that can be chosen in the gamesetup

main_pack = pack.Pack(1, 'main_pack', 'testdescription', cards.main_white_cards, cards.main_black_cards)

my_packs = [main_pack]