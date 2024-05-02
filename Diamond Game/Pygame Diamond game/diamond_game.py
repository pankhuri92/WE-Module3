import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Colors
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)

# Card dimensions
CARD_WIDTH = 5
CARD_HEIGHT = 10

# Font settings
font = pygame.font.Font(None, 24)

# Function to load card images
def load_card_images():
    card_images = {}
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    for suit in suits:
        for rank in range(2, 15):
            file_name = f"images/{rank}_of_{suit.lower()}.svg"  # Adjust path as needed
            card_images[(rank, suit)] = pygame.image.load(file_name)
    return card_images

# Function to create a deck of cards
def create_deck():
    deck = [(rank, suit) for rank in range(2, 15) for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']]
    random.shuffle(deck)
    return deck

# Function to determine the winner of the round
def determine_winner(user_bid_value, computer_bid_value, diamond_value):
    if user_bid_value > computer_bid_value:
        return 'user'
    elif user_bid_value < computer_bid_value:
        return 'computer'
    else:
        return 'tie'

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("The Diamond Game")

# Load card images
card_images = load_card_images()

# Initialize user and computer decks
user_deck, computer_deck = create_deck()[:13], create_deck()[:13]  # Select first 13 cards for each player

# Initialize round counter
round_counter = 0

# Main game loop
running = True
while running and round_counter < 13:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Start a new round
    round_counter += 1
    diamond_card = random.choice(create_deck())  # Select a random diamond card
    user_bid_card = None
    computer_bid_card = random.choice(computer_deck)  # Computer bids randomly

    # Display diamond card in the center
    window.fill(GREEN)
    window.blit(card_images[diamond_card], ((WINDOW_WIDTH - CARD_WIDTH) // 2, (WINDOW_HEIGHT - CARD_HEIGHT) // 2))

    # Draw user's cards at the bottom
    x_user = (WINDOW_WIDTH - (len(user_deck) * (CARD_WIDTH + 10))) // 2  # Center the cards
    for card in user_deck:
        window.blit(card_images[card], (x_user, WINDOW_HEIGHT - CARD_HEIGHT - 50))
        x_user += CARD_WIDTH + 10

    # Draw computer's cards at the top
    x_computer = (WINDOW_WIDTH - (len(computer_deck) * (CARD_WIDTH + 10))) // 2  # Center the cards
    for card in computer_deck:
        window.blit(card_images[card], (x_computer, 50))
        x_computer += CARD_WIDTH + 10

    # Display user score
    user_score_text = font.render(f"User score: {sum(card[0] for card in user_deck)}", True, WHITE)
    window.blit(user_score_text, (50, 50))

    # Display computer score
    computer_score_text = font.render(f"Computer score: {sum(card[0] for card in computer_deck)}", True, WHITE)
    window.blit(computer_score_text, (WINDOW_WIDTH - computer_score_text.get_width() - 50, 50))

    # Update the display
    pygame.display.update()

    # User bidding
    user_bid_card = None
    while not user_bid_card:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, card in enumerate(user_deck):
                    card_x = (WINDOW_WIDTH - (len(user_deck) * (CARD_WIDTH + 10))) // 2 + i * (CARD_WIDTH + 10)
                    card_y = WINDOW_HEIGHT - CARD_HEIGHT - 50
                    if card_x <= mouse_pos[0] <= card_x + CARD_WIDTH and card_y <= mouse_pos[1] <= card_y + CARD_HEIGHT:
                        user_bid_card = card
                        break

    # Determine the winner of the round
    winner = determine_winner(user_bid_card[0], computer_bid_card[0], diamond_card[0])

    # Update scores and remove bid cards from decks
    if winner == 'user':
        user_deck.remove(user_bid_card)
        user_deck.append(diamond_card)
    elif winner == 'computer':
        computer_deck.remove(computer_bid_card)
        computer_deck.append(diamond_card)
    else:
        user_deck.remove(user_bid_card)
        user_deck.append(diamond_card)
        computer_deck.remove(computer_bid_card)
        computer_deck.append(diamond_card)

# Quit Pygame
pygame.quit()
sys.exit()
