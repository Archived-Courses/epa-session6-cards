# epa-session6-card game

## Problem
* Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck
* Write a normal function without using lambda, zip, and map function to create 52 cards in a deck
* Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game. (TODO)


## Description
It contains the following files:

card_game.py - This file contains the methods for creating the 52 deck of cards
test_card_game.py - This file contains the tests using the framework pytest.

### find_possible_combinations(list1, list2) 
Given any 2 lists of varying or equal length, the function returns a merged list of all possible combinations

### create_deck_using_single_expr()
Returns a deck of 52 cards created using a single expression. The function makes use of lambda, map and zip functions. 

### create_deck_manually()
Returns a deck of 52 cards created using nested for loops

### create_deck_list_comprehension()
Returns a deck of cards created using list comprehension
