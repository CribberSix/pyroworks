import pygame
import sys
from src.Rocket import Rocket

screen = pygame.display.set_mode((900, 600))
rockets = []
rocket_every_x_frames = 8
counter = 0

while True:
    counter += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if counter % rocket_every_x_frames == 0:
        rockets.append(Rocket())

    # Render
    pygame.display.get_surface().fill((41, 50, 65))
    for r in rockets[:]:
        r.render()
        if r.dead:
            rockets.remove(r)
    pygame.time.Clock().tick(30)
    pygame.display.flip()
