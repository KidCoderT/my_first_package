"""
=================== TEST 1 ===================

Tests The HorizontalScrollingBG class
only for a continues scrolling. Also Checks
whether the image.scale_image method works

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

scale_factor = 1.3
SCREEN_WIDTH, SCREEN_HEIGHT = 288, 512
SCREEN = pygame.display.set_mode(
    (SCREEN_WIDTH * scale_factor, SCREEN_HEIGHT * scale_factor)
)
DISPLAY = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test Scene 1")

speed = 0
bg_img = pygame.image.load("assets/background-day.png")
bg = ui.HorizontalScrollingBG(bg_img, speed)


def reset_scene():
    global bg, speed
    bg = ui.HorizontalScrollingBG(bg_img, speed)


def run():
    global bg, speed
    clock = pygame.time.Clock()

    while True:
        DISPLAY.fill((255, 0, 0))

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

        bg.render(DISPLAY)
        bg.update()

        SCREEN.blit(image.scale_image(DISPLAY, scale_factor), (0, 0))
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    run()
