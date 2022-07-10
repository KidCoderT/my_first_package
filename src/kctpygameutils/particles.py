class ParticlesContainers:
    """the main particle system container class.
    a singular instance can hold one type of particle
    and so you can create multiple instances to create multiple
    different particles even in the same project
    """

    def __init__(self):
        self.particles = []

    def emit(self, screen) -> int:
        """the main update method for a particle.
        this  both draws and updates the particle as well as remove it too

        Args:
            screen (_type_): _description_
        """
        to_remove = []

        for particle in self.particles:
            particle.render(screen)
            particle.update()

            if particle.should_remove():
                to_remove.append(particle)

        for particle in to_remove:
            self.particles.remove(particle)

        return len(to_remove)

    def add_particle(self, particle):
        """This is the method to call when you want to add a particle.
        and this can be of any type

        Args:
            particle (any): the  particle to add
        """
        self.particles.append(particle)


class ImageParticleObject:
    """This is used for particles where an image is involved
    this is the bare minimum setup required when dealing with
    images and here for x and y you will be dealing with the img_rect.

    to make an image particle object you will need to override almost
    all the methods other than maybe the render method that is unless
    you need a more sophisticated / custom render method

    Args:
        img (pygame.surface.Surface): the image of the particle
        x (int | float): the center x position of the particle
        y (int | float): the center y position of the particle
    """

    def __init__(self, img, x, y):
        self.img = img
        self.rect = img.get_rect(center=(x, y))

    def update(self):
        """the particles container will run this every frame to update the image"""
        pass

    def render(self, screen):
        """this will be used to render the image by the particles container.
        if you want to customize the render to oo you can override this method"""
        screen.blit(self.img, self.rect.topleft)

    def should_remove(self):
        """this is where the remove logic is placed and this method will be called
        by the particles container to check whether or not the particle should be removed

        this must return a bool value for the particle system to work"""
        pass


class ShapeParticleObject:
    """This is used for particles where a shape is involved
    this is the bare minimum setup required when dealing with
    particles  with shapes and here you will mainly  be dealing with x and y.

    To create a shape particle object you will need to override
    all the methods this time

    Args:
        x (int | float): the x position of the particle
        y (int | float): the y position of the particle
    """

    def __init__(self, x, y):
        self.x, self.y = x, y

    def update(self):
        """the particles container will run this every frame to update the image"""
        pass

    def render(self, screen):
        """this will be used to render the shape by the particles container."""
        pass

    def should_remove(self):
        """this is where the remove logic is placed and this method will be called
        by the particles container to check whether or not the particle should be removed

        this must return a bool value for the particle system to work"""
        pass
