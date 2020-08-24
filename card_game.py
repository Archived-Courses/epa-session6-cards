""" 
Problem:

Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck
Write a normal function without using lambda, zip, and map function to create 52 cards in a deck
Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game. 

"""
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']





def find_possible_combinations(list1, list2):
    """
    Function that returns all combinations possible with two lists

    Inputs:
        list 1
        list 2

    Returns:
        a list containing all possible combinations of list1 and list2

    """

    return [item for sublist in list(map(lambda x : list(zip(list2, [x] * len(list2))), list1)) for item in sublist]    


def create_deck_using_single_expr():
    """
    Function that uses a single expression including lambda, zip and map functions to create 52 cards in a deck

    Returns:
        a list containing 52 cards in a deck

    """

    return find_possible_combinations(suits, vals)


def create_deck_manually():
    """
    Function that creates 52 cards in a deck by for loop

    Returns:
        a list containing 52 cards in a deck

    """
    
    deck = []

    for suit in suits:
        for val in vals:
            deck.append((val, suit))

    return deck


def create_deck_list_comprehension():
    """
    Function that creates 52 cards in a deck with list comprehension

    Returns:
        a list containing 52 cards in a deck

    """

    return [(val, card) for val in vals for card in suits]
