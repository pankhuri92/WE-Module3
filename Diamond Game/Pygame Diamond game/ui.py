import pygame
import sys
from gameplay import Game
import random

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Diamond Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load card images
def load_card_images():
    card_images = {}
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    for suit in suits:
        for rank in range(2, 15):
            file_name = f"images/{rank}_of_{suit.lower()}.svg"  # Adjust path as needed
            card_images[(rank, suit)] = pygame.image.load(file_name)
    return card_images

# Function to draw the computer and user decks
def draw_decks(computer_deck, user_deck):
    # Draw computer deck
    for i, card in enumerate(computer_deck):
        x = (SCREEN_WIDTH // 2) - (len(computer_deck) * 40) + (i * 80)
        y = 50
        screen.blit(card, (x, y))
    
    # Draw user deck
    for i, card in enumerate(user_deck):
        x = (SCREEN_WIDTH // 2) - (len(user_deck) * 40) + (i * 80)
        y = SCREEN_HEIGHT - 150
        screen.blit(card, (x, y))

# Function to draw the diamond card
def draw_diamond_card(diamond_card):
    x = (SCREEN_WIDTH // 2) - 36
    y = (SCREEN_HEIGHT // 2) - 48
    screen.blit(diamond_card, (x, y))

# Function to display scores
def display_scores(player_score, computer_score):
    font = pygame.font.Font(None, 36)
    player_text = font.render(f"User Score: {player_score}", True, BLACK)
    computer_text = font.render(f"Computer Score: {computer_score}", True, BLACK)
    screen.blit(player_text, (20, 20))
    screen.blit(computer_text, (20, SCREEN_HEIGHT - 60))

# Main game loop
def main():
    # Load card images
    card_images = load_card_images()

    # Initialize the game
    game = Game("Player")

    # Main loop
    while True:
        screen.fill(WHITE)

        # Draw computer and user decks
        draw_decks(game.computer.hand, game.player.hand)

        # Draw diamond card
        diamond_card = card_images[game.diamond_card]
        draw_diamond_card(diamond_card)

        # Display scores
        display_scores(game.user_points, game.computer_points)

        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
