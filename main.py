import blackjack

print("Welcome to Blackjack.")
print("This is a simplied version of Blackjack. The rules are simple:")
print("1. Both players are dealt 2 cards facing up.")
print("2. Either players can choose to either\n\tstand[s] (not do anything) \n\tor \n\thit[h] (get another card).")
print("3. Number cards' values are their numbers, 10s and face cards' values are 10, and ace's value is 11.")
print("4. A player automatically wins when their cards' values add up to 21.")
print("5. A player automatically loses when their cards' values goes over 21.")
print("Note: Both players can choose stand unlimited amount of times in this game.\n")
print("Are you ready? [y/n]")
main = input()

gameIsOn = main == "y"

if gameIsOn:
    blackjack = blackjack.BlackJack()
    blackjack.play()