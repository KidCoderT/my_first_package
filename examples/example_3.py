"""
=================== TEST 3 ===================

Tests The HorizontalScrollingBG class moves
only when sprite moves. Also Shows example for
Making Parallax Effect

============================================== 
"""

import sys
import pygame
from pygame.locals import QUIT

sys.path.append("../")
from kct_pygame_tools import ui, image

pygame.init()


def run():
    scale_factor = 2
    SCREEN_WIDTH, SCREEN_HEIGHT = 480 * scale_factor, 272 * scale_factor
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Test Scene 3")

    acceleration = 20
    friction = 0.7
    max_speed = 40

    speed = 0

    layers = [
        ui.HorizontalScrollingBG(
            image.load_and_scale(
                "./assets/parallax-demon-woods-far-trees.png", scale_factor
            ),
            3,
        ),
        ui.HorizontalScrollingBG(
            image.load_and_scale(
                "./assets/parallax-demon-woods-mid-trees.png", scale_factor
            ),
            max_speed * 0.6,
        ),
        ui.HorizontalScrollingBG(
            image.load_and_scale(
                "./assets/parallax-demon-woods-close-trees.png", scale_factor
            ),
            max_speed,
        ),
    ]

    clock = pygame.time.Clock()

    while True:
        screen.fill((218, 94, 83))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            speed += acceleration
        elif pressed[pygame.K_LEFT]:
            speed -= acceleration
        speed *= friction

        for layer in layers:
            layer.render(screen)

            if speed > 2 or speed < -2:
                layer.moving_update(speed, 50)

        print(speed)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    run()
