import copy
from enum import Enum

class Player:
    movement = Enum('movement', 'up down left right')

    def __init__(self, posX, posY, size):
        self.tailLength = 2
        self.tail = []
        self.position = [posX, posY]
        self.previousPosition = copy.copy(self.position)
        self.size = size
        self.direction = self.movement.up

    def setMoveDirection(self, movement):
        if movement == self.movement.up and self.direction != self.movement.down or \
           movement == self.movement.down and self.direction != self.movement.up or \
           movement == self.movement.left and self.direction != self.movement.right or \
           movement == self.movement.right and self.direction != self.movement.left:
            self.direction = movement

    def grow(self):
        self.tailLength += 1

    def update(self):
        self.previousPosition = copy.copy(self.position)
        if self.direction == self.movement.up:
            self.position[1] -= 1
        elif self.direction == self.movement.down:
            self.position[1] += 1
        elif self.direction == self.movement.left:
            self.position[0] -= 1
        elif self.direction == self.movement.right:
            self.position[0] += 1
        #print(self.position[0], self.position[1])

    def setShape(self, shape):
        self.shape = shape

    class TailPart:

        def __init__(self, previous):
            self.previous = previous
            self.size = self.previous.size
            self.position = [self.previous.previousPosition[0], self.previous.previousPosition[1]]
            self.previousPosition = copy.copy(self.position)

        def update(self):
            self.previousPosition = copy.copy(self.position)
            self.position = [self.previous.previousPosition[0], self.previous.previousPosition[1]]

        def setShape(self, shape):
            self.shape = shape