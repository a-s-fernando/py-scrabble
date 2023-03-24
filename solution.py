# Calculate the score for a word. The score is the sum of the points for the letters that make up a word. For example: GUARDIAN = 2 + 1 + 1 + 1 + 2 + 1 + 1 + 1 = 10.
# Assign seven tiles chosen randomly from the English alphabet to a player's rack.
# In the real game, tiles are taken at random from a 'bag' containing a fixed number of each tile. Assign seven tiles to a rack using a bag containing the above distribution.

# Find a valid word formed from the seven tiles. A list of valid words can be found in dictionary.txt.
# Find the longest valid word that can be formed from the seven tiles.
# Find the highest scoring word that can be formed.
# Find the highest scoring word if any one of the letters can score triple.
# For discussion: how would we adapt our solution for a multiplayer environment?

# 1	E, A, I, O, N, R, T, L, S, U
# 2	D, G
# 3	B, C, M, P
# 4	F, H, V, W, Y
# 5	K
# 8	J, X
# 10	Q, Z
from random import randint

LETTER_VALUES = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
}
STARTING_BAG = ['E']*12 + ['A']*9 + ['I']*9 + ['O']*7 + ['N']*6 + ['R']*6 + ['T']*6\
    + ['L']*4 + ['S']*4 + ['U']*4 + ['D']*4 + ['G']*3 + ['B']*2 + ['C']*2 + ['M']*2\
    + ['P']*2 + ['F']*2 + ['H']*2 + ['V']*2 + ['W']*2 + ['Y'] * 2\
    + ['K'] + ['J'] + ['X'] + ['Q'] + ['Z']

print(STARTING_BAG)


def calculate_score(input: str) -> int:
    total = 0
    for letter in input:
        total += LETTER_VALUES[letter]
    return total


def populate_rack_randomly() -> list:
    player_rack = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for _ in range(0, 7):
        player_rack.append(alphabet[randint(0, len(alphabet)-1)])
    return player_rack


def populate_rack_from_bag(bag: list) -> list:
    player_rack = []
    for _ in range(0, 7):
        player_rack.append(bag.pop(randint(0, len(bag)-1)))
    return player_rack


def validate_word(word: str) -> bool:
    pass
