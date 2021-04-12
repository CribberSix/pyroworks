import pygame
import sys
from random import randint
from src.Rocket import Rocket

screen = pygame.display.set_mode((900, 600))


def create_randomized_rocket():
    x = randint(0, pygame.display.get_surface().get_width())
    y = pygame.display.get_surface().get_height()
    speed = randint(10, 35)
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    return Rocket(x, y, speed, color)


rockets = []
rocket_every_x_frames = 8
c = 0
while True:
    c += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.get_surface().fill((41, 50, 65))

    if c % rocket_every_x_frames == 0:
        rockets.append(create_randomized_rocket())
    for r in rockets[:]:
        r.render()
        if r.dead:
            rockets.remove(r)

    pygame.time.Clock().tick(30)
    pygame.display.flip()
