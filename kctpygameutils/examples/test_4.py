"""
=================== TEST 4 ===================

Tests The Blit and rotate method, pallete swap,
multiline text methods, blit_text_center method
and outline method

============================================== 
"""
import random
import sys
import pygame
from pygame.locals import QUIT
from .. import ui, image

pygame.init()


def run():
    SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Test Scene 4")

    saw = image.load_and_scale("./assets/saw.png", 3)
    saw_rect = saw.get_rect(center=((SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.2)))
    angle = 0

    saw.set_colorkey((0, 0, 0))

    all_colors = [
        "#AFBBC3",
        "#DAF3D3",
        "#99DBD3",
        "#B96E54",
        "#A14744",
        "#6C3C4C",
        "#443444",
        "#9C4C4C",
        "#704048",
        "#60E0D8",
        "#858D99",
        "#D8E1E4",
        "#4CC4CC",
        "#5CE273",
        "#E4C997",
        "#CF9E6E",
        "#7C4048",
    ]

    saw_color = "#241C34"

    font = pygame.font.SysFont("arial", 15)
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    text_2 = "Girl i hope you understand but i wanted to hold hand but cant"

    text_box = (105, 260, 500, 500)

    clock = pygame.time.Clock()

    while True:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                old_color = saw_color
                new_color = random.choice(all_colors)
                print(old_color, new_color)
                saw = image.palette_swap(saw, old_color, new_color, colorkey=(0, 0, 0))
                saw_color = new_color

        angle += 2
        image.blit_and_rotate_center(screen, saw, saw_rect.topleft, angle)
        ui.draw_text_multilined(screen, text, (0, 0, 0), text_box, font)
        image.outline_mask(saw, (saw_rect.x, 410), screen, saw_color)
        ui.blit_text_center(screen, font, text_2, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.8)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    run()
