import random

class DeckOfCards:
    suits = ["♥","♠","♦","♣"]
    cards = ["11","2","3","4","5","6","7","8","9","10","J","Q","K"]
    deck = []
    drawn_deck = []

    def __init__(self):
        self.populate_deck()
        self.shuffle()

    def populate_deck(self):
        for suit in self.suits:
            for card in self.cards:
                self.deck.append(suit+card)

    def draw(self):
        drawn_card = self.deck.pop()
        self.drawn_deck.append(drawn_card)
        return drawn_card

    def shuffle(self):
        random.shuffle(self.deck)

    def reset(self):
        self.deck.clear()
        self.populate_deck()
        self.drawn_deck.clear()
