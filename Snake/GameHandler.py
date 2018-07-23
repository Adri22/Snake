import math
import random
from Window import *
from ObjectHandler import *
#from World import *
from Player import *
from Dot import *

class GameHandler:
    worldSize = 30
    delay = 100
    obstacles = Enum('obstacles', 'dot tail wall')
    directions = {
        37: Player.movement.left, 
        38: Player.movement.up, 
        39: Player.movement.right, 
        40: Player.movement.down}

    def __init__(self):
        self.player = Player(
            math.ceil((self.worldSize - 1) / 2),
            math.ceil((self.worldSize - 1) / 2),
            Window.tileSize)
        self.window = Window(self.worldSize)
        self.window.master.bind("<KeyPress>", self.keyDown)
        self.player.setShape(
            self.window.canvas.create_rectangle(
                self.player.position[0] * self.player.size,
                self.player.position[1] * self.player.size,
                self.player.position[0] * self.player.size + self.player.size,
                self.player.position[1] * self.player.size + self.player.size,
                fill = "black",
                outline = ""))
        self.objectHandler = ObjectHandler(self.window.canvas)

    def start(self):
        self.createDot()
        self.objectHandler.add(self.player)
        self.process()
        self.window.open()

    def process(self):
        if self.isCollidingWith() == self.obstacles.dot:
            self.objectHandler.remove(self.dot)
            self.player.grow()
            self.createDot()
        elif self.isCollidingWith() == self.obstacles.tail or \
             self.isCollidingWith() == self.obstacles.wall:
            print("game over")
            self.window.stop()
        while len(self.player.tail) < self.player.tailLength:
            if len(self.player.tail) == 0:
                previous = self.player
            else:
                previous = self.player.tail[len(self.player.tail) - 1]
            self.player.tail.append(self.player.TailPart(previous))
            self.objectHandler.joinList(self.player.tail)
            newTailPart = self.player.tail[len(self.player.tail) - 1]
            newTailPart.setShape(
                self.window.canvas.create_rectangle(
                    newTailPart.position[0] * newTailPart.size,
                    newTailPart.position[1] * newTailPart.size,
                    newTailPart.position[0] * newTailPart.size + newTailPart.size,
                    newTailPart.position[1] * newTailPart.size + newTailPart.size,
                    fill = "black",
                    outline = ""))
            print("extend tail - current length:", len(self.player.tail))
        self.objectHandler.update()
        self.objectHandler.render()
        self.window.canvas.after(self.delay, self.process)

    def createDot(self):
        positionValid = False
        reservedPositions = []
        reservedPositions.append([self.player.position[0], self.player.position[1]])
        for tailPart in self.player.tail:
            reservedPositions.append([tailPart.position[0], tailPart.position[1]])
        while not positionValid:
            dotPosition = [
                random.randint(0, self.worldSize - 1),
                random.randint(0, self.worldSize - 1)]
            for position in reservedPositions:
                if dotPosition[0] != position[0] and dotPosition[1] != position[1]:
                    positionValid = True
                else:
                    positionValid = False
                    break
        self.dot = Dot(
            dotPosition[0],
            dotPosition[1],
            Window.tileSize)
        self.dot.setShape(
            self.window.canvas.create_rectangle(
                self.dot.position[0] * self.dot.size,
                self.dot.position[1] * self.dot.size,
                self.dot.position[0] * self.dot.size + self.dot.size,
                self.dot.position[1] * self.dot.size + self.dot.size,
                fill = "blue",
                outline = ""))
        self.objectHandler.add(self.dot)

    def isCollidingWith(self):
        if self.player.position[0] == self.dot.position[0] and \
           self.player.position[1] == self.dot.position[1]:
            print("collides with dot")
            return self.obstacles.dot
        elif self.player.position[0] >= self.worldSize or \
             self.player.position[1] >= self.worldSize or \
             self.player.position[0] < 0 or \
             self.player.position[1] < 0:
            print("collides with wall")
            return self.obstacles.wall
        else:
            for tailPart in self.player.tail:
                if self.player.position[0] == tailPart.position[0] and \
                   self.player.position[1] == tailPart.position[1]:
                    print("collides with tail")
                    return self.obstacles.tail
        return None

    def keyDown(self, event):
        self.player.setMoveDirection(self.directions.get(event.keycode, self.directions.get(38)))
        print("key down:", event.keycode, "- direction:", self.player.direction)