import pygame
import math
import random
from mold import Mold


# constants
WIDTH = 800
BLACK = (0, 0, 0)
N_MOLDS = 5000


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Slime Mould")
    pygame.display.set_icon(pygame.image.load("./assets/icon.png"))

    # Create a semi-transparent surface
    fade_surface = pygame.Surface((WIDTH, WIDTH))
    fade_surface.set_alpha(1)
    fade_surface.fill(BLACK)

    molds = [Mold(screen) for _ in range(N_MOLDS)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw fading effect
        screen.blit(fade_surface, (0, 0))

        for mold in molds:
            mold.update()
            mold.display()

        pygame.display.flip()
        pygame.time.delay(0)

    pygame.quit()

if __name__ == "__main__":
    main()
