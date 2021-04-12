import pygame
from .Particle import Particle
from random import randint


class Rocket:

    def __init__(self, x, y, speed, color):
        self.screen = pygame.display.get_surface()
        self.x = x
        self.y = y
        self.color = color
        self.r = 5
        self.speed = speed
        self.max_speed = 10
        self.acceleration = 0.95
        self.risen = False
        self.spawned_particles = False
        self.dead = False
        self.trail_colours = [(45, 45, 45), (60, 60, 60), (75, 75, 75), (125, 125, 125), (150, 150, 150),
                              (175, 175, 175)]

        self.particles = []

    def render(self):
        """
         Renders the rocket and subsequent particles.

        :return: None
        """
        # Rendering rocket
        if not self.risen:
            pygame.draw.circle(self.screen, self.color, (self.x, int(self.y)), self.r)
            self.render_trail()

        # Rendering explosion particles
        for p in self.particles:
            p.render()
            if p.done:
                self.particles.remove(p)

        # calculate new speed, height and positioning
        self.speed = self.speed * self.acceleration

        # Stages: moving upwards, creating particles
        if self.speed > 1:
            self.y -= self.speed
        else:
            self.risen = True

        if self.risen and not self.spawned_particles:
            self.create_particles()

        if self.risen and len(self.particles) == 0:
            self.dead = True

    def create_color(self):
        """
        Creates a randomized color based on the initial color of the rocket.
        :return:
        """

        def limit_var(n):
            return max(min(255, n), 0)

        variant = 75
        c0 = limit_var(randint(self.color[0] - variant, self.color[0] + variant))
        c1 = limit_var(randint(self.color[1] - variant, self.color[1] + variant))
        c2 = limit_var(randint(self.color[2] - variant, self.color[2] + variant))

        return c0, c1, c2

    def create_particles(self):
        """
        Creates 100 particles spraying outward from the rocket's explosion point.

        :return: None
        """
        self.spawned_particles = True
        for _ in range(0, 100):
            acc_x = randint(-5, 5)
            acc_y = randint(-5, 5) * (abs(abs(acc_x) - 5) * 0.6)  # particles in the middle spray further

            color = self.create_color()
            r = randint(1, 4)
            reduce_mod = randint(4, 8)
            p = Particle(self.x, int(self.y),
                         acc_x,
                         acc_y,
                         color,
                         r,
                         reduce_mod)
            self.particles.append(p)

    def render_trail(self):
        """
        Calculates and renders the rocket's trail.
        The first trail points increase in size, but towards the end of the trail the size decreases again.

        :return: None
        """
        y = self.y + (8 * (self.speed / self.max_speed))
        size = 1
        for i, tc in enumerate(self.trail_colours):
            pygame.draw.circle(self.screen, tc, (self.x, int(y)),  size)
            y = y + (8 * (self.speed / self.max_speed))
            if i <= len(self.trail_colours) / 4:
                size += 1
            else:
                size -= 1
                if size == 0:
                    size = 1
