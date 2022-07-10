"""
The module has methods that can transform an image,
use sprite sheets, swap_image colors and give an outline to the image
"""

import pygame
from PIL import ImageColor
from pygame.surface import Surface as img_surface


def scale_image(img: img_surface, factor: float) -> img_surface:
    """Scales the image width and height by a given factor and returns it

    Args:
        img (img_surface): the image to scale
        factor (float): the factor to scale the image by

    Returns:
        img_surface: the transformed image
    """

    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_and_rotate_center(
    win: img_surface, image: img_surface, top_left: tuple, angle: int
):
    """Taking a Straight image rotates it and draws it onto the screen

    Args:
        win (img_surface): the window to draw the image on
        image (img_surface): the image to rotate and draw
        top_left (tuple[float | int]): contains the top left position of the image
        angle (int): the angle to rotate

    Returns:
        : _description_
    """

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


def outline_mask(
    img: img_surface,
    loc: tuple | list,
    display: img_surface,
    colors=(255, 255, 255),
):
    """Draws an outline for the given image

    Args:
        img (img_surface): the image to outline
        loc (tuple | list): the locations of the image
        display (img_surface): the screen to draw the outline onto
        colors (tuple, optional): the color of the outline. Defaults to (255, 255, 255).
    """

    mask = pygame.mask.from_surface(img)
    mask_outline = mask.outline()
    n = 0
    for point in mask_outline:
        mask_outline[n] = (point[0] + loc[0], point[1] + loc[1])
        n += 1
    pygame.draw.polygon(display, colors, mask_outline, 3)


def palette_swap(
    surf: img_surface, old_color: str, new_color: str, colorkey=(0, 0, 0)
) -> img_surface:
    """Swaps one color inside an image to another color and returns the color changed image

    Args:
        surf (img_surface): the image to change
        old_color (str): the color to swap in hex form
        new_color (str): the color to swap to in hex form
        colorkey (tuple, optional): removes a certain color from the after image. Defaults to black

    Returns:
        img_surface: The image to swap
    """

    img_copy = img_surface(surf.get_size())
    img_copy.fill(ImageColor.getcolor(new_color, "RGB"))  # type: ignore
    surf.set_colorkey(ImageColor.getcolor(old_color, "RGB"))  # type: ignore
    img_copy.blit(surf, (0, 0))
    img_copy.set_colorkey(colorkey)
    return img_copy


def load_and_scale(filename: str, scale_factor: float, alpha: int = 255) -> img_surface:
    """Easy way to load and scale an image

    Args:
        filename (str): the image link
        scale_factor (float): the factor to scale by
        alpha (int, optional): sets the alpha value. Defaults to 255.

    Returns:
        img_surface: the image
    """
    img = pygame.image.load(filename)
    img = scale_image(img, scale_factor)
    img.set_alpha(alpha)

    return img


class spritesheet(object):
    """Used to Handle Sprite sheets in pygame"""

    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()

    def image_at(self, rectangle, colorkey=None, scale_factor=1):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return scale_image(image, scale_factor)

    def images_at(self, rects, colorkey=None):
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey=None):
        tups = [
            (rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
            for x in range(image_count)
        ]
        return self.images_at(tups, colorkey)

    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image
