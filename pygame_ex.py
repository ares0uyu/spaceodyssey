import sys

import pygame
import random
import math
from pygame.locals import QUIT

class Star:
    def __init__(self, screen, screenSize, index):
        self.size = 1
        self.color = (255,255,255)

        self.center = {
            'x' : screen.get_width() / 2,
            'y' : screen.get_height() / 2
        }

        self.radius = 0
        self.theta = 0

        self.screen = screen
        self.screenSize = screenSize

        self.init(index)

    def getLimitDistance(self):
        return int(math.sqrt(math.pow(self.center['x'], 2) + math.pow(self.center['y'], 2)))

    def init(self, index):
        self.radius = float(random.randint(0, self.getLimitDistance()))
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        self.degree = (360 / 50) * index
        self.theta = float(self.degree) * math.pi / 180

    def draw(self, color):
        x = self.center['x'] + self.radius * math.cos(self.theta)
        y = self.center['y'] + self.radius * math.sin(self.theta)

        pygame.draw.circle(self.screen, color, [x,y], self.size)

    def move(self):

        self.radius += 1 + (float(self.radius) / 10)
        self.size = 1 + (self.radius / 100)

        self.draw(self.color)

        if self.radius > self.getLimitDistance():
            self.radius = float(random.randint(0, self.getLimitDistance()))


screenSize = {
    'width' : 1024,
    'height' : 768
}

pygame.init()
screen = pygame.display.set_mode((screenSize['width'], screenSize['height']))
pygame.display.set_caption('Space Odyssey')

stars = []
for i in range(0, 50):
    star = Star(screen, screenSize, i)
    stars.append(star)

count = 0
delay = 10000
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    clock.tick(30)

    screen.fill((0, 0, 0))

    for star in stars:
        star.move()

    pygame.display.update()




