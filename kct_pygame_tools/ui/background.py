"""
Contains Methods that can handle Scrolling Background and
Custom Scrolling Backgrounds also.
"""

from abc import ABC, abstractmethod
from pygame.surface import Surface as surface
import pygame


class ScrollingBG(ABC):
    """The Basis For the Scrolling Background including both horizontal,
    Vertical and Any Custom Background if needed

    Properties:
        1. img -> the repeated image
        2. rect -> the calculated Rectangular representation of the image
        3. speed -> the speed to move by
        4. is_negative -> whether the speed is negative or not

        5. bg_1 -> the first backgrounds top left position
        6. bg_2 -> the second backgrounds top left position
    """

    def __init__(self, img: surface, speed: float | int):
        self.img = img
        self.rect = img.get_rect()
        self.speed = speed
        self.is_negative = self.speed < 0

        self.bg_1 = pygame.Vector2(0, 0)
        self.bg_2 = pygame.Vector2(0, 0)
        self.bg_3 = pygame.Vector2(0, 0)

    def render(self, display: surface):
        """Renders the image in the 3 different positions for the illusion of repetition

        Args:
            display (pygame.Surface): the screen to blit the illusion on
        """
        display.blit(self.img, (self.bg_1.x, self.bg_1.y))
        display.blit(self.img, (self.bg_2.x, self.bg_2.y))
        display.blit(self.img, (self.bg_3.x, self.bg_3.y))

    @abstractmethod
    def update(self):
        pass


class HorizontalScrollingBG(ScrollingBG):
    """
    The Horizontal scrolling class
    Extends: ScrollingBG

    Can be used to create a Forever Scrolling Background or
    A scrolling along with the player kinda background
    """

    def __init__(self, img: surface, speed: float | int):
        super().__init__(img, speed)
        self.bg_1.x = -self.rect.width
        self.bg_3.x = self.rect.width
        self.img_width = self.rect.width

    def update(self):
        """
        Used when you want to create a basic forever
        scrolling background
        """

        self.move_screens(self.speed)
        self.check_and_reset_position()

    def moving_update(
        self, player_speed: float, max_player_speed: float, min_player_speed: float = 0
    ):
        """
        Used when you want to create a background that moves
        dynamically

        Args:
            player_speed (float): the speed to the player
            max_player_speed (float): the max speed of the player
            min_player_speed (float): the min speed of the player. Defaults to 0
        """

        n = round(player_speed)
        for num in range(1, n):
            if n % num == 0:
                break
        else:
            n += 1

        start1 = min_player_speed
        stop1 = max_player_speed
        start2 = 0.0
        stop2 = 1.0

        speed = (
            self.speed * ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2
        )

        self.move_screens(speed)

        if n != 0:
            self.is_negative = player_speed < 0

        self.check_and_reset_position()

    def move_screens(self, speed: int | float):
        self.bg_1.x += speed
        self.bg_2.x += speed
        self.bg_3.x += speed

    def check_and_reset_position(self):
        """
        Checks wheter the screens position are out of bounds
        and fixes them accordingly
        """

        if self.is_negative:
            if self.bg_1.x <= -self.img_width:
                self.bg_1.x = self.bg_3.x + self.img_width
            elif self.bg_2.x <= -self.img_width:
                self.bg_2.x = self.bg_1.x + self.img_width
            elif self.bg_3.x <= -self.img_width:
                self.bg_3.x = self.bg_2.x + self.img_width
        else:
            if self.bg_1.x >= self.img_width:
                self.bg_1.x = self.bg_3.x - self.img_width
            elif self.bg_2.x >= self.img_width:
                self.bg_2.x = self.bg_1.x - self.img_width
            elif self.bg_3.x >= self.img_width:
                self.bg_3.x = self.bg_2.x - self.img_width


class VerticalScrollingBG(ScrollingBG):
    """
    The Vertical scrolling class
    Extends: ScrollingBG

    Can be used to create a Forever Scrolling Background Only.
    For custom Moving you need to create your own move with player
    Vertically Scrolling BG you can extend this class and change the update
    function
    """

    def __init__(self, img: surface, speed: float | int):
        super().__init__(img, speed)
        self.bg_1.y = -self.rect.height
        self.bg_3.y = self.rect.height
        self.img_height = self.rect.height

    def update(self):
        """
        Updated the Positions Each Frame and reset them if they go
        out of bounds
        """

        self.move_screens(self.speed)
        self.check_and_reset_position()

    def custom_update(self, speed):
        """You can use override this method when creating a custom
        Vertical Scrolling Class

        Args:
            speed: Speed to move screens by
        """
        self.move_screens(self.speed)

    def move_screens(self, speed: int | float):
        self.bg_1.y += speed
        self.bg_2.y += speed
        self.bg_3.y += speed

    def check_and_reset_position(self):
        """
        Checks whether the screens position are out of bounds
        and fixes them accordingly
        """

        if self.is_negative:
            if self.bg_1.y <= -self.img_height:
                self.bg_1.y = self.bg_3.y + self.img_height
            elif self.bg_2.y <= -self.img_height:
                self.bg_2.y = self.bg_1.y + self.img_height
            elif self.bg_3.y <= -self.img_height:
                self.bg_3.y = self.bg_2.y + self.img_height
        else:
            if self.bg_1.y >= self.img_height:
                self.bg_1.y = self.bg_3.y - self.img_height
            elif self.bg_2.y >= self.img_height:
                self.bg_2.y = self.bg_1.y - self.img_height
            elif self.bg_3.y >= self.img_height:
                self.bg_3.y = self.bg_2.y - self.img_height
