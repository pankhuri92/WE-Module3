# strategy.py

import random

# Function to create a deck of cards for a specific suit
def create_deck(suit):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for rank in ranks]
    return deck

# Function to initialize player decks
def initialize_players():
    suits = ['Hearts', 'Clubs', 'Spades']
    user_suit, computer_suit = random.sample(suits, k=2)
    user_deck = create_deck(user_suit)
    computer_deck = create_deck(computer_suit)
    return user_deck, computer_deck

# Function to create a deck of diamond cards
def create_diamond_deck():
    diamond_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    diamond_deck = [(rank, 'Diamonds') for rank in diamond_ranks]
    random.shuffle(diamond_deck)
    return diamond_deck

# Function to calculate bid value based on card rank
def calculate_bid_value(card):
    rank = card[0]
    rank_value_mapping = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
    return rank_value_mapping.get(rank, 0)

# Function to display the card
def display_card(card):
    print(f"The diamond card is: {card[0]} of {card[1]}")

# Function for user bidding
def user_bid(user_deck):
    print("Your cards:")
    for card in user_deck:
        print(f"{card[0]} of {card[1]}")
    while True:
        bid_card_rank = input("Choose a card rank to bid (e.g., 2, 3, Jack): ").strip().title()
        bid_card = (bid_card_rank, 'Hearts')  # Assume user's suit is always hearts
        if bid_card not in user_deck:
            print("Invalid card rank. Please choose from your cards.")
        else:
            user_deck.remove(bid_card)
            return bid_card

# Function for computer bidding
def computer_bid(computer_deck):
    bid_card = random.choice(computer_deck)
    computer_deck.remove(bid_card)
    return bid_card

# Function to determine the winner of the round
def determine_winner(user_bid_value, computer_bid_value, diamond_value):
    if user_bid_value > computer_bid_value:
        print("You win the bid!")
        return 'user'
    elif user_bid_value < computer_bid_value:
        print("Computer wins the bid!")
        return 'computer'
    else:
        print("It's a tie! Both players share the diamond value.")
        return 'tie'

# Function to play the game
def play_game():
    user_deck, computer_deck = initialize_players()
    diamond_deck = create_diamond_deck()
    user_points = 0
    computer_points = 0

    while diamond_deck:
        diamond_card = diamond_deck.pop()
        display_card(diamond_card)

        user_bid_card = user_bid(user_deck)
        user_bid_value = calculate_bid_value(user_bid_card)

        computer_bid_card = computer_bid(computer_deck)
        computer_bid_value = calculate_bid_value(computer_bid_card)

        print(f"User bid: {user_bid_card[0]} of {user_bid_card[1]} (Value: {user_bid_value})")
        print(f"Computer bid: {computer_bid_card[0]} of {computer_bid_card[1]} (Value: {computer_bid_value})")

        winner = determine_winner(user_bid_value, computer_bid_value, calculate_bid_value(diamond_card))

        if winner == 'user':
            user_points += calculate_bid_value(diamond_card)
            print(f"You gain {calculate_bid_value(diamond_card)} points!")
        elif winner == 'computer':
            computer_points += calculate_bid_value(diamond_card)
            print(f"Computer gains {calculate_bid_value(diamond_card)} points!")
        else:
            points = calculate_bid_value(diamond_card) / 2
            user_points += points
            computer_points += points
            print(f"Both players gain {points} points!")

    print("\nGame over!")
    print("Total points:")
    print(f"User: {user_points}")
    print(f"Computer: {computer_points}")

    if user_points > computer_points:
        print("Congratulations! You win!")
    elif user_points < computer_points:
        print("Computer wins!")
    else:
        print("It's a tie!")

# Main function to start the game
def main():
    print("Welcome to the Diamond Game!")
    play_game()

if __name__ == "__main__":
    main()
