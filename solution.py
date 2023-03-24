# Find the longest valid word that can be formed from the seven tiles.
# Find the highest scoring word that can be formed.
# Find the highest scoring word if any one of the letters can score triple.
# For discussion: how would we adapt our solution for a multiplayer environment?
from random import randint


LETTER_VALUES = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
}


with open('dictionary.txt') as f:
    VALID_WORDS = [line.strip('\n') for line in f]


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


def generate_starting_bag() -> list:
    return ['E']*12 + ['A']*9 + ['I']*9 + ['O']*7 + ['N']*6 + ['R']*6 + ['T']*6\
        + ['L']*4 + ['S']*4 + ['U']*4 + ['D']*4 + ['G']*3 + ['B']*2 + ['C']*2 + ['M']*2\
        + ['P']*2 + ['F']*2 + ['H']*2 + ['V']*2 + ['W']*2 + ['Y'] * 2\
        + ['K'] + ['J'] + ['X'] + ['Q'] + ['Z']


def populate_rack_from_bag(bag: list) -> list:
    player_rack = []
    for _ in range(0, 7):
        player_rack.append(bag.pop(randint(0, len(bag)-1)))
    return player_rack


def validate_word(word: str) -> bool:
    if word in VALID_WORDS:
        return True
    return False
