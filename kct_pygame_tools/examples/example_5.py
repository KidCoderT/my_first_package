"""
=================== TEST 5 ===================

Tests The Particle System with images and also
tests the spritesheet class

============================================== 
"""
import random
import sys
import pygame
from pygame.locals import QUIT
from .. import particles, image

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700


class LeafParticle(particles.ImageParticleObject):
    def __init__(self, img, scatter=False):
        x, y = random.randint(50, int(SCREEN_WIDTH - 50)), -random.randint(-50, 100)
        if scatter:
            x, y = random.randint(50, int(SCREEN_WIDTH - 50)), -random.randint(
                50, int(SCREEN_HEIGHT - 50)
            )

        super().__init__(img, x, y)
        self.img = image.scale_image(self.img, 5)
        self.vel = [random.randint(-2, 2), random.randint(1, 2)]
        self.img.set_alpha(200)

    def update(self):
        self.rect.x += self.vel[0] + random.uniform(-1.0, 1.0)
        self.rect.y += self.vel[1] + random.uniform(-1.0, 1.0)

    def should_remove(self):
        return (
            self.rect.x < -10
            or self.rect.x > SCREEN_WIDTH + 10
            or self.rect.y > SCREEN_HEIGHT + 10
        )


def run():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Test Scene 4")

    leaf_particle_manager = particles.ParticlesContainers()
    leaves_spritesheet = image.spritesheet("assets/leaves.png")
    leaf_images = leaves_spritesheet.load_strip((0, 0, 4, 4), 4, (0, 0, 0))

    leaf_particle_manager.particles = [
        LeafParticle(random.choice(leaf_images), True) for _ in range(120)
    ]

    for _ in range(100):
        removed_amount = leaf_particle_manager.emit(screen)
        for __ in range(removed_amount):
            leaf_particle_manager.add_particle(LeafParticle(random.choice(leaf_images)))

    clock = pygame.time.Clock()
    while True:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        removed_amount = leaf_particle_manager.emit(screen)
        for i in range(removed_amount):
            leaf_particle_manager.add_particle(LeafParticle(random.choice(leaf_images)))

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    run()
