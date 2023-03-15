import pygame
from math import *
import numpy as np

scale = 3
angle = 0

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


def main(angle):
    while True:
        projected2d = []

        for point in points:
            rotated2d = np.dot(rotateZ(angle), point.reshape(3, 1))
            rotated2d = np.dot(rotateY(angle), rotated2d)
            rotated2d = np.dot(rotateX(angle), rotated2d)
            projected2d.append(np.dot(projection_matrix, rotated2d) * scale)

        for obj in projected2d:
            print(obj)

        for objY in range(-5 * scale, 5 * scale):
            for objX in range(-5 * scale, 5 * scale):
                isPoint = False
                for projection in projected2d:
                    if int(projection[0][0]) == objX and int(projection[1][0]) == objY:
                        isPoint = True

                if isPoint:
                    print("@", end=" ")
                else:
                    print(".", end=" ")
            print()

        print()
        angle += 0.01


main(angle)