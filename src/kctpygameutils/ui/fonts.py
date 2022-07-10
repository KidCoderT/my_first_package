import pygame


def blit_text_center(
    win: pygame.surface.Surface,
    font: pygame.font.Font,
    text: str,
    x: int | float,
    y: int | float,
    color=(0, 0, 0),
):
    """Unlike how you would usualy blit a text from the
    top left of the text box. Here this method allows you to blit
    the text center onto the position

    Args:
        win (pygame.surface.Surface): the window to blit on
        font (pygame.font.Font): the font to use for the text
        text (str): the text coontent
        x (int | float): the center x position to be blit on
        y (int | float): the center y position to blit on
        color: the color to blit the text with
    """

    render = font.render(text, True, color)
    win.blit(
        render,
        (
            x - render.get_width() / 2,
            y - render.get_height() / 2,
        ),
    )


def draw_text_multilined(
    surface: pygame.surface.Surface,
    text: str,
    color: tuple,
    rect: pygame.Rect | tuple,
    font: pygame.font.Font,
    anti_alias=False,
    background=None,
):
    """This method automatically wraps text inside a pygame rect object
    and then blits it onto the screen.

    Args:
        surface (pygame.surface.Surface): the window to blit onto
        text (str): the text to wrap
        color (tuple): the color to blit the text with
        rect (pygame.Rect | tuple): the rect inside which to wrap the text
        font (pygame.font.Font): the font too use
        anti_alias (bool, optional): wheter the font has anti_alias. Defaults to False.
        background (_type_, optional): the background color of the font. Defaults to None.
    """
    rect = pygame.Rect(rect)
    y = rect.top
    line_spacing = 3

    # get the height of the font
    font_height = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + font_height > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if background:
            image = font.render(text[:i], True, color, background)
            image.set_colorkey(background)
        else:
            image = font.render(text[:i], anti_alias, color)

        surface.blit(image, (rect.left, y))
        y += font_height + line_spacing

        # remove the text we just blitted
        text = text[i:]
