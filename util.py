# Import sleep to show output for a period of time.
from time import sleep

# Import only system from os.
from os import system, name

# Clears the terminal screen
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Prints the message and waits for 1 second.
def display(message):
    print(message)
    sleep(1)

# Prints the given hand.
def print_hand(cards, sleep_duration = 0):
    for card in cards:
        if card[1:] == "11":
            print("[" + card[0] + "A" + "] ", end = '')
        else:
            print("[" + card + "] ", end = '')

    print("")
    sleep(sleep_duration)