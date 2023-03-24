from solution import *


def test_calculate_score():
    assert calculate_score("GUARDIAN") == 10


def test_valid_random_rack():
    player_rack = populate_rack_randomly()
    assert len(player_rack) == 7
    for letter in player_rack:
        assert letter.isalpha()


def test_valid_rack_from_bag():
    bag = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    player_rack = populate_rack_from_bag(bag)
    assert len(player_rack) == 7
    for letter in player_rack:
        assert letter.isalpha()
    for tile in bag:
        assert tile in player_rack


def test_valid_word():
    pass


def test_invalid_word():
    pass
