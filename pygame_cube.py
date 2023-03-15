import pygame
from math import *
import numpy as np
import random

WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (64, 64, 64)
SYMBOLS_COLOR = (255, 255, 255)

scale = 750
circle_pos = [WIDTH / 2, HEIGHT / 2]
angle = 0

pygame.init()

pygame.display.set_caption("3D Cube")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])


def creatingSurface():
    points = []

    for z in range(-2, 2):
        for y in range(-2, 2):
            for x in range(-2, 2):
                points.append(np.matrix([x / 10, y / 10, z / 10]))

    return points


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


points = creatingSurface()

clock = pygame.time.Clock()
while True:

    clock.tick(60)
    screen.fill(BACKGROUND_COLOR)

    projected2d = []

    counter = 0
    for point in points:
        counter += 1
        rotated2d = np.dot(rotateZ(angle), point.reshape(3, 1))
        rotated2d = np.dot(rotateY(angle), rotated2d)
        rotated2d = np.dot(rotateX(angle), rotated2d)

        projected2d.append(np.dot(projection_matrix, rotated2d))

    for obj in projected2d:
        x = int(obj[0][0] * scale) + circle_pos[0]
        y = int(obj[1][0] * scale) + circle_pos[1]

        font = pygame.font.SysFont("symbol", 15)
        text = font.render("#", True, SYMBOLS_COLOR)
        screen.blit(text, (x, y))
        """for yKoef in range(0, 8):
            for xKoef in range(0, 8):
                screen.blit(text, (x + xKoef * 10, y + yKoef * 10))"""

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
