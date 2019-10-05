# Import deck_of_cards for the playing cards.
import deck_of_cards

# Import random for probability calculation.
import random

# Import util for non-game related functions.
import util

class BlackJack:
    # Returns the sum of the hand.
    def sum_of_hand(self, cards):
        total = 0
        faces = ["J","Q","K"]
        
        for card in cards:
            if card[1:] in faces:
                total += 10
            else:
                total += int(card[1:])
        
        return total

    # Checks the victory status of the given hand.
    # Returns None if the hand sums up to over 21.
    # Returns True if the hand sums up to 21.
    # Returns False if the hand sums up to under 21.
    def hand_wins(self, cards):
        total = self.sum_of_hand(cards)

        if total > 21:
            return None
        if total == 21:
            return True
        else:
            return False

    # Determines whether the CPU should hit or stand.
    # The probability of the CPU choosing to hit is proportional to
    # the value it needs to reach 21.
    # In other words, CPU should hit when exactly or more than 7 away from 21.
    def should_hit(self, cards):
        total = self.sum_of_hand(cards)

        # Amount needed to get to 21 / 21.
        probability = (21 - total) / 21

        # Increases the change of CPU choosing to hit by making the CPU 
        # take a bit of a risk.
        probability += 0.2
        
        chance = random.randint(1, 101) / 100

        if probability >= chance:
            return True
        else:
            return False

    # If a hand wins or loses, returns (True, winning_hand).
    # If no hand wins or loses, return (False, None).
    def game_is_over(self, cpu_hand, player_hand):
        cpu_status = self.hand_wins(cpu_hand)
        player_status = self.hand_wins(player_hand)

        # If CPU loses or the player wins.
        if cpu_status == None or player_status == True:
            return (True, player_hand)
        # If CPU wins or the player loses.
        elif cpu_status == True or player_status == None:
            return (True, cpu_hand)
        # If no one wins or loses yet.
        else:
            return (False, None)

    # Play the turn for the player.
    # Returns True if choice made is invalid, otherwise None.
    def play_player_turn(self, deck, player_hand):
        print("\nStand or Hit? [s/h]")
        player_choice = input()
        
        if player_choice == "s":
            util.display("\nYou chose to stand.")
            choice_invalid = False

        elif player_choice == "h":
            util.display("\nYou chose to hit!")
            
            new_card = deck.draw()
            print("\nYou drew ", end="")
            util.print_hand([new_card], 1)

            player_hand.append(new_card)
            choice_invalid = False

        else:
            print("\nNot a valid choice.")
            return True

    # Play the turn for the CPU.
    def play_cpu_turn(self, deck, cpu_hand):
        util.display("\nJack Black is deciding...")
        cpu_should_hit = self.should_hit(cpu_hand)
        if cpu_should_hit:
            util.display("\nJack Black chose to hit!")

            new_card = deck.draw()
            print("\nJack Black drew ", end ="")
            self.print_hand([new_card], 1)

            cpu_hand.append(new_card)
        else:
            util.display("\nJack Black chose to stand.")
            
    # Starts and plays blackjack.
    def play(self):
        deck = deck_of_cards.DeckOfCards()
        util.clear()
        
        # Give out CPU hand.
        cpu_hand = []
        cpu_hand.append(deck.draw())
        cpu_hand.append(deck.draw())

        # Give out player hand.
        player_hand = []
        player_hand.append(deck.draw())
        player_hand.append(deck.draw())

        # Checks victory or loss for the initial hands.
        game_status = self.game_is_over(cpu_hand, player_hand)

        player_turn = True

        # While game has not been won or lost by anyone.
        while not game_status[0]:
            util.clear()
            print("Jack Black:")
            util.print_hand(cpu_hand)

            print("You:")
            util.print_hand(player_hand)
            
            choice_invalid = True
            player_choice = ""

            # Choice must be either h and s.
            while choice_invalid:
                if player_turn:
                    choice_invalid = self.play_player_turn(deck, player_hand)
                    player_turn = False
                else:
                    choice_invalid = self.play_cpu_turn(deck, cpu_hand)
                    player_turn = True

            game_status = self.game_is_over(cpu_hand, player_hand)

        util.clear()

        # If the CPU won.
        if game_status[1] == cpu_hand:
            print("Jack Black wins: ", end = "")
            util.print_hand(cpu_hand)
            print("\nYou lose: ", end = "")
            util.print_hand(player_hand)

        # If the player won.
        elif game_status[1] == player_hand:
            print("You win: ", end = "")
            util.print_hand(player_hand)
            print("\nJack Black loses: ", end = "")
            util.print_hand(cpu_hand)
    


        



