# Blackjack

This is a simplified version of Blackjack coded in Python.

## Prerequisites

1. Check if python is installed by running:
```
python3 --version
```
2. If not, click [here](https://realpython.com/installing-python/).

## Playing

1. Clone this repository.
2. Run this line into your terminal:

```
python3 main.py
```

3. Follow instructions on the terminal.

## Rules
1. Both players are dealt 2 cards facing up.
2. Either players can choose to either stand or hit.
3. Number cards' values are their numbers, 10s and face cards' values are 10, and ace's value is 11.
4. A player automatically wins when their cards' values add up to 21.
5. A player automatically loses when their cards' values goes over 21.
Note: Both players can choose stand unlimited amount of times in this game.

## Design Choices
Code was refactored into different functions and files to minimize redundancy and maximize readability. 

4 files are required to run this game: deck_of_cards.py, blackjack.py, util.py, and main.py.
- deck_of_cards.py
  - Contains the class DeckOfCards. Contains methods to intuitively manipualate a deck using functions such as shuffle() and draw().
- blackjack.py
  - Contains the class Blackjack. Contains methods that pertain to the game itself such as play_cpu_turn(), play_player_turn(), and play().
- util.py
  - Contains all functions that are not class-specific such as clear() to clear the terminal screen.
- main.py
  - Main file that needs to be ran in order for the game to start.
  

## Built With

* [Python](https://www.python.org/) - The main programming language.

## Author

* **Peter Lee**

## Acknowledgments

* Credits to [GeeksforGeeks](https://www.geeksforgeeks.org/clear-screen-python/) for code to clear the terminal.
