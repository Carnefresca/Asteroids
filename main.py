from player import Player
from constants import *
import pygame

def main():
    pygame.init
    Carne = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius= PLAYER_RADIUS)
    Clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        Carne.update(dt)
        screen.fill(0)
        Carne.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()