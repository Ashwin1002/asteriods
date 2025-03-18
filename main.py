import pygame
import sys
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from gameover import show_game_over


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background = pygame.image.load("resources/images/space_background.png")  
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # limiting key event update to updatable group
    updatable = pygame.sprite.Group()

    # limiting shape drawable group
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    
    # Font Setup
    font = pygame.font.Font(None, 36)

    # Score Variable
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
 
        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game over!")
                print(f"Your final score is {score}!")
                # sys.exit()
                restart = show_game_over(screen, score)
                if restart:
                    return main()  # Restart game

            for shot in shots:
                if asteroid.detect_collision(shot):
                    shot.kill()
                    score += asteroid.split(screen)

        screen.blit(background, (0, 0))
        
        for obj in drawable:
            obj.draw(screen)

         # Render Score
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        dt = clock.tick(60) / 1000 
if __name__ == "__main__":
    main()