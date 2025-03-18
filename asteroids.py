import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

EXPLOSION_FRAMES = [pygame.image.load(f"resources/images/explosion/explosion{i}.png") for i in range(11)] 
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.exploding = False  # Explosion state
        self.explosion_frame = 0  # Track explosion animation frame
        self.frame_delay = 5  # Adjust for slower or faster explosion
        self.counter = 0  # Frame counter

    def draw(self, screen):
        if self.exploding:
            print("drawing explosion animation")
            frame = EXPLOSION_FRAMES[self.explosion_frame]
            screen.blit(frame, (self.position.x - frame.get_width() // 2, 
                                self.position.y - frame.get_height() // 2))
            explosion_sound = pygame.mixer.Sound("resources/sounds/explosion.wav")
            explosion_sound.play()
        else:
            pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        if self.exploding:
            self.counter += 1
            if self.counter % self.frame_delay == 0:
                self.explosion_frame += 1  # Move to the next frame
                if self.explosion_frame >= len(EXPLOSION_FRAMES):  # Animation finished
                    self.kill()  # Remove asteroid
        else:
            self.position += self.velocity * dt
    
    def split(self, screen):
        """ Splits asteroid into two smaller pieces or explodes if too small. """
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.reset_exploding_animation(screen)
            return 5  # Score for small asteroid

        self.kill()
        
        random_angle = random.uniform(20, 50)
        e1 = self.velocity.rotate(random_angle)
        e2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = e1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = e2 * 1.2

        return 0
    
    def reset_exploding_animation(self, screen):
        """ Starts the explosion animation instead of instantly removing the asteroid. """
        self.exploding = True
        self.explosion_frame = 0
        self.counter = 0  # Reset animation counter
        self.draw(screen)