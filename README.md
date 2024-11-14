# Card Game Framework

**Author:** Zach Khan  
**Date:** March 31, 2023  

This program provides a basic framework for a card game, where it can keep track of the location of cards within a deck and assign them to players. It supports handling multiple hands and can be expanded for more complex card game logic.

## Program Overview

The card game framework performs the following actions:
- Initializes a deck of cards
- Assigns cards randomly to the player and the computer
- Tracks card locations and displays each card's location in the deck or in a player's hand

## Features

- **Random Card Assignment**: Cards are dealt randomly to each player from the deck.
- **Deck and Hand Display**: The program can display the entire deck with card names and locations, as well as individual hands for each player.

## How It Works

The program uses several constants and lists:
- `NUMCARDS`: Total number of cards (52).
- `DECK`, `PLAYER`, `COMP`: Constants representing the deck, player, and computer.
- `cardLoc`: A list that stores the location of each card (deck, player, or computer).
- `suitName` and `rankName`: Lists containing the names of suits and ranks for easy card identification.

### Main Functions

- **`clearDeck()`**: Initializes all cards to be in the deck.
- **`assignCard(player)`**: Randomly assigns an available card to the specified player (player or computer).
- **`showDeck()`**: Displays the entire deck with each card’s name and location.
- **`showHand(player)`**: Displays the cards held by a specific player.

## Usage

To run the program, execute the following command:

```bash
python cardGame.py
```
The program will: 

- Initialize the deck. 
- Deal 5 random cards to both the player and the computer. 
- Display the location of all cards and show each player’s hand. 

## Example Output

```bash
Location of all cards 
#  Card                  Location
1  Ace of hearts         deck
...
Displaying player hand:
Three of clubs
Nine of diamonds
...
Displaying r hand:
King of spades
Two of hearts
...
```

## Future Improvements

- Expand to handle multiple players. 
- Implement game rules for a specific card game. 
- Add support for additional card actions like drawing and discarding. 

This framework can serve as the foundation for developing a more sophisticated card game simulation in Python.
