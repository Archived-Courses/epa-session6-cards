import pytest
from card_game import *



def test_possible_combinations():
    l2 = ['a', 'b', 'c']
    l1 = ['1', '2']

    assert [('a', '1'), ('b', '1'), ('c', '1'), ('a', '2'), ('b', '2'), ('c', '2')] == find_possible_combinations(l1,l2)




def test_doc_possible_combinations():
    assert """
    Function that returns all combinations possible with two lists

    Inputs:
        list 1
        list 2

    Returns:
        a list containing all possible combinations of list1 and list2

    """ == find_possible_combinations.__doc__


def test_create_deck():
    assert [('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('5', 'spades'), ('6', 'spades'), ('7', 'spades'), ('8', 'spades'), ('9', 'spades'), ('10', 'spades'), ('jack', 'spades'), ('queen', 'spades'), ('king', 'spades'), ('ace', 'spades'), ('2', 'clubs'), ('3', 'clubs'), ('4', 'clubs'), ('5', 'clubs'), ('6', 'clubs'), ('7', 'clubs'), ('8', 'clubs'), ('9', 'clubs'), ('10', 'clubs'), ('jack', 'clubs'), ('queen', 'clubs'), ('king', 'clubs'), ('ace', 'clubs'), ('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts'), ('5', 'hearts'), ('6', 'hearts'), ('7', 'hearts'), ('8', 'hearts'), ('9', 'hearts'), ('10', 'hearts'), ('jack', 'hearts'), ('queen', 'hearts'), ('king', 'hearts'), ('ace', 'hearts'), ('2', 'diamonds'), ('3', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'), ('6', 'diamonds'), ('7', 'diamonds'), ('8', 'diamonds'), ('9', 'diamonds'), ('10', 'diamonds'), ('jack', 'diamonds'), ('queen', 'diamonds'), ('king', 'diamonds'), ('ace', 'diamonds')] == create_deck_using_single_expr()

    assert 52 == len(create_deck_using_single_expr())


def test_create_deck_manual():
    assert [('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('5', 'spades'), ('6', 'spades'), ('7', 'spades'), ('8', 'spades'), ('9', 'spades'), ('10', 'spades'), ('jack', 'spades'), ('queen', 'spades'), ('king', 'spades'), ('ace', 'spades'), ('2', 'clubs'), ('3', 'clubs'), ('4', 'clubs'), ('5', 'clubs'), ('6', 'clubs'), ('7', 'clubs'), ('8', 'clubs'), ('9', 'clubs'), ('10', 'clubs'), ('jack', 'clubs'), ('queen', 'clubs'), ('king', 'clubs'), ('ace', 'clubs'), ('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts'), ('5', 'hearts'), ('6', 'hearts'), ('7', 'hearts'), ('8', 'hearts'), ('9', 'hearts'), ('10', 'hearts'), ('jack', 'hearts'), ('queen', 'hearts'), ('king', 'hearts'), ('ace', 'hearts'), ('2', 'diamonds'), ('3', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'), ('6', 'diamonds'), ('7', 'diamonds'), ('8', 'diamonds'), ('9', 'diamonds'), ('10', 'diamonds'), ('jack', 'diamonds'), ('queen', 'diamonds'), ('king', 'diamonds'), ('ace', 'diamonds')] == create_deck_manually()


def test_create_deck_list_comprehension():
    assert 52 == len(create_deck_list_comprehension())


