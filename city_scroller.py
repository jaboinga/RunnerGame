"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
    return random.choice(colors)

minBuildingWidth = 10
maxBuildingWidth = 50
minBuildingHeight = 10



class Building():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height), 0)


    def move(self, speed):
       self.x -= speed



class Scroller(object):

    def __init__(self, width, height, base, color, speed):
        self.width = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.row = []
        
        self.add_buildings()
        
    def add_building(self, x):
        randWidth = random.randint(minBuildingWidth, maxBuildingWidth)
        randHeight = random.randint(minBuildingHeight, self.height)
        self.row.append(Building(x, self.base - randHeight, randWidth, randHeight, self.color))

    def add_buildings(self):
        currentSpot = 0
        while(currentSpot < self.width):
            self.add_building(currentSpot)
            currentSpot += self.row[len(self.row) - 1].width
    
    def draw_buildings(self, screen):
        for building in self.row:
            building.draw(screen)

    def move_buildings(self):
        for building in self.row:
            building.move(self.speed)
            if(building.x <= -1 * building.width):
                self.row.remove(building)
        if(self.row[-1].x + self.row[-1].width <= self.width + self.speed):
            self.add_building(self.row[-1 ].x + self.row[-1].width)