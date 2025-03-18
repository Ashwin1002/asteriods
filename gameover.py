import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import sys


def show_game_over(screen, score):
    """ Displays a Game Over popup with options to restart or exit """

    game_over_sound = pygame.mixer.Sound("resources/sounds/game_over.wav")
    game_over_sound.play() # play game over sound

    popup_width, popup_height = 400, 300
    popup_x, popup_y = (SCREEN_WIDTH - popup_width) // 2, (SCREEN_HEIGHT - popup_height) // 2

    font_large = pygame.font.Font(None, 50)
    font_medium = pygame.font.Font(None, 36)

    # Colors
    RED = (200, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (100, 100, 100)
    LIGHT_GRAY = (180, 180, 180)

    while True:
        screen.fill(BLACK)
        pygame.draw.rect(screen, GRAY, (popup_x, popup_y, popup_width, popup_height), border_radius=15)

        # "Game Over" Text
        game_over_text = font_large.render("GAME OVER", True, RED)
        screen.blit(game_over_text, (popup_x + 100, popup_y + 30))

        # Score Text
        score_text = font_medium.render(f"Your final score is {score}!", True, WHITE)
        screen.blit(score_text, (popup_x + 80, popup_y + 80))

        # Draw Buttons
        play_again_button = pygame.Rect(popup_x + 100, popup_y + 150, 200, 50)
        exit_button = pygame.Rect(popup_x + 100, popup_y + 220, 200, 50)

        pygame.draw.rect(screen, LIGHT_GRAY, play_again_button, border_radius=10)
        pygame.draw.rect(screen, LIGHT_GRAY, exit_button, border_radius=10)

        # Button Text
        play_again_text = font_medium.render("Play Again", True, BLACK)
        exit_text = font_medium.render("Exit", True, BLACK)

        screen.blit(play_again_text, (popup_x + 140, popup_y + 160))
        screen.blit(exit_text, (popup_x + 175, popup_y + 230))

        pygame.display.flip()

        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_again_button.collidepoint(mouse_pos):
                    game_over_sound.stop()  # Stop game over sound
                    return True  # Restart game
                elif exit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()