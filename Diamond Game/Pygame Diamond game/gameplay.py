# gameplay.py

import random
from strategy import user_bid, computer_bid, determine_winner, calculate_bid_value

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []  # Initialize an empty hand

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def remove_card_from_hand(self, card):
        if card in self.hand:
            self.hand.remove(card)
        else:
            raise ValueError("Card not found in player's hand.")

class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.computer = Player("Computer")
        self.diamonds = self.create_diamond_deck()
        self.user_points = 0
        self.computer_points = 0

    def create_diamond_deck(self):
        diamond_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        diamond_deck = [(rank, 'Diamonds') for rank in diamond_ranks]
        random.shuffle(diamond_deck)
        return diamond_deck

    def draw_diamond_card(self):
        return self.diamonds.pop()

    def score_round(self, diamond_card, user_bid_value, computer_bid_value):
        if user_bid_value > computer_bid_value:
            self.user_points += self.calculate_bid_value(diamond_card)
        elif user_bid_value < computer_bid_value:
            self.computer_points += self.calculate_bid_value(diamond_card)
        else:
            points = self.calculate_bid_value(diamond_card) / 2
            self.user_points += points
            self.computer_points += points

    @staticmethod
    def calculate_bid_value(card):
        return calculate_bid_value(card)

    def determine_winner(self):
        return determine_winner(self.user_points, self.computer_points)

    def user_bid(self):
        return user_bid(self.player.hand)

    def computer_bid(self):
        return computer_bid(self.computer.hand)

