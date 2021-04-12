import pygame


class Particle:

    def __init__(self, x, y, acc_x, acc_y, color, r, reduce_mod=10):
        self.screen = pygame.display.get_surface()
        self.x = x
        self.y = y
        self.acc_x = acc_x
        self.acc_y = acc_y
        self.acc_y_original = acc_y
        self.color = color
        self.r = r
        self.reduce_counter = 0
        self.reduce_mod = reduce_mod
        self.done = False

    def render(self):
        """
        Renders the particle and reduces it's size every couple of frames.

        :return: None
        """
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.r)
        self.move()

        self.reduce_counter += 1
        if self.reduce_counter % self.reduce_mod == 0:
            self.r -= 1
            if self.r == 0:
                self.done = True

    def move(self):
        """
        Calculates and updates the position of the particle.
        :return:
        """
        self.x += self.acc_x
        self.y += self.acc_y
        self.y += 1

        self.acc_x = self.acc_x * 0.925  # reduce acc_x constantly so it gets slower towards the edges

        if self.acc_y < 0:  # goes upwards -> reduce over time
            self.acc_y += abs(self.acc_y_original * 0.1)


