"""
=================== TEST 2 ===================

Tests The VerticalScrollingBG class. Also Checks
whether the image.load_and_scale method works

When the thing starts, press the up and down
arrow keys to update speed of the background.
as by default its set to 0 so it doesn't move at all

============================================== 
"""

import sys
import pygame
from pygame.locals import QUIT, KEYDOWN

sys.path.append("../")
from kct_pygame_tools import ui, image

pygame.init()

SCALE_AMOUNT = 0.5

SCREEN_WIDTH, SCREEN_HEIGHT = 1920 * SCALE_AMOUNT, 1080 * SCALE_AMOUNT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test Scene 2")

speed = 0
bg_img = image.load_and_scale("assets/space.png", SCALE_AMOUNT)
bg = ui.VerticalScrollingBG(bg_img, speed)


def reset_scene():
    global bg, speed
    bg = ui.VerticalScrollingBG(bg_img, speed)


def run():
    global bg, speed
    clock = pygame.time.Clock()

    while True:
        screen.fill((255, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_UP:
                    speed -= 1
                    reset_scene()
                elif event.key == pygame.K_DOWN:
                    speed += 1
                    reset_scene()

        print(speed)

        bg.render(screen)
        bg.update()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    run()
