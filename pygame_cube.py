import pygame
from math import *
import numpy as np

WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (64, 64, 64)
SYMBOLS_COLOR = (255, 255, 255)

scale = 100
circle_pos = [WIDTH/2, HEIGHT/2]
angle = 0

pygame.init()

pygame.display.set_caption("3D Cube")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Math and Matrix
points = [np.matrix([-1, -1, 1]),
          np.matrix([1, -1, 1]),
          np.matrix([1, 1, 1]),
          np.matrix([-1, 1, 1]),
          np.matrix([-1, -1, -1]),
          np.matrix([1, -1, -1]),
          np.matrix([1, 1, -1]),
          np.matrix([-1, 1, -1])]

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])


# Martix rotation
def rotateX(angle):
    rotation = np.matrix([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]
    ])
    return rotation


# Rotations
def rotateY(angle):
    rotation = np.matrix([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]
    ])
    return rotation


def rotateZ(angle):
    rotation = np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ])
    return rotation


clock = pygame.time.Clock()
while True:

    clock.tick(60)
    screen.fill(BACKGROUND_COLOR)

    for point in points:
        rotated2d = np.dot(rotateZ(angle), point.reshape(3, 1))
        rotated2d = np.dot(rotateY(angle), rotated2d)
        rotated2d = np.dot(rotateX(angle), rotated2d)

        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]

        font = pygame.font.SysFont("symbol", 15)
        text = font.render("#", True, SYMBOLS_COLOR)
        screen.blit(text, (x, y))

    angle += 0.01

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    pygame.display.update()