""" cardGame.py
    Zach Khan
    March 31, 2023
    
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
#from random import *
import random

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "r")

def main():
  clearDeck()

  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)

  showDeck()
  showHand(PLAYER)
  showHand(COMP)

# Clears the deck
def clearDeck():
    # Puts the number of cards in the deck
    for i in range(NUMCARDS):
        cardLoc[i] == DECK

# Defines each card with a number, then displays the name and location of each card
def showDeck():
    print("\nLocation of all cards \n#  Card                  Location")
    card = 0
    for location in cardLoc:
        rank = card % 13
        suit = int(card/13)
        card = card + 1
        print (f"{card}  {rankName[rank]} of {suitName[suit]} \t {playerName[location]}")

# Assigns cards randomly to the player and the computer
def assignCard(player):
    deal = True
    while deal:
        card = random.randint(0,51)
        if cardLoc[card] == DECK:
            cardLoc[card] = player
            deal = False

# Displays the hands of the player and the computer
def showHand(player):
    print ("\nDisplaying {} hand:" .format(playerName[player]))
    for card in range(0,51):
        if cardLoc[card] == player:
            rank = card % 13
            suit = int(card / 13)
            print (rankName[rank], "of", suitName[suit])

main()