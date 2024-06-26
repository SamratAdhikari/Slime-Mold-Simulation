import math
import pygame
import random

# constants
WIDTH = 800
BLACK = (100, 100, 100)
RED = (128, 0, 0)
# GREY = (104, 109, 118)
GREEN = (91, 128, 75)



CENTER_X = WIDTH // 2
CENTER_Y = WIDTH // 2
STD_DEV_X = 100
STD_DEV_Y = 100

class Mold:
    def __init__(self, surface):
        # self.x = random.randrange(WIDTH)
        # self.y = random.randrange(WIDTH)
        self.x = random.gauss(CENTER_X, STD_DEV_X) % WIDTH
        self.y = random.gauss(CENTER_Y, STD_DEV_Y) % WIDTH

        self.surface = surface
        self.r = .5

        self.heading = math.radians(random.randrange(360))
        self.rotatingAngle = math.radians(45)
        self.vx = math.cos(self.heading)
        self.vy = math.sin(self.heading)


        self.rSensorPos = pygame.math.Vector2(0, 0)
        self.lSensorPos = pygame.math.Vector2(0, 0)
        self.cSensorPos = pygame.math.Vector2(0, 0)
        self.sensorAngle = math.radians(45)
        # self.sensorDist = random.randrange(40)
        self.sensorDist = 40
        self.sensorHeadingX = math.cos(self.heading + self.sensorAngle)
        self.sensorHeadingY = math.sin(self.heading + self.sensorAngle)


    def luminance(self, color):
        return 0.299 * color.r + 0.587 * color.g + 0.114 * color.b


    def comparePixels(self, r, l, c):
        lum_r = self.luminance(r)
        lum_l = self.luminance(l)
        lum_c = self.luminance(c)

        if (lum_c > lum_l) and (lum_c > lum_r):
            self.heading += 0

        elif (lum_c < lum_l) and (lum_c < lum_r):
            if random.random() < 0.5:
                self.heading += self.rotatingAngle

        elif (lum_l > lum_r):
            self.heading -= self.rotatingAngle

        elif (lum_r > lum_l):
            self.heading += self.rotatingAngle


    def getSensorPos(self, sensor, angle):
        sensor.x = (self.x + self.sensorDist*math.cos(angle)) % WIDTH
        sensor.y = (self.y + self.sensorDist*math.sin(angle)) % WIDTH


    def update(self):
        # change direction
        self.vx = math.cos(self.heading)
        self.vy = math.sin(self.heading)
        self.x = (self.x + self.vx) % WIDTH
        self.y = (self.y + self.vy) % WIDTH

        # right
        self.getSensorPos(self.rSensorPos, self.heading+self.sensorAngle)
        
        # left
        self.getSensorPos(self.lSensorPos, self.heading-self.sensorAngle)
        
        # center
        self.getSensorPos(self.cSensorPos, self.heading)


        # pixels
        r = pygame.Surface.get_at(self.surface, (int(self.rSensorPos.x % WIDTH), int(self.rSensorPos.y % WIDTH)))
        l = pygame.Surface.get_at(self.surface, (int(self.lSensorPos.x % WIDTH), int(self.lSensorPos.y % WIDTH)))
        c = pygame.Surface.get_at(self.surface, (int(self.cSensorPos.x % WIDTH), int(self.cSensorPos.y % WIDTH)))

        # compare pixels
        self.comparePixels(r, l, c)



    def display(self):
        # actual mold
        _params = (self.x-self.r, self.y-self.r, self.r*2, self.r*2)
        pygame.draw.ellipse(surface=self.surface, color=BLACK, rect=_params)

        # mold direction
        _start = (self.x, self.y)
        _end = (self.x + 3*self.r*self.vx, self.y + 3*self.r*self.vy)
        pygame.draw.line(surface=self.surface, color=GREEN, start_pos=_start, end_pos=_end)

        # mold silhouettes
        '''
        _params = (self.rSensorPos.x-self.r, self.rSensorPos.y-self.r, self.r*2, self.r*2)
        pygame.draw.ellipse(surface=self.surface, color=RED, rect=_params)

        _params = (self.lSensorPos.x-self.r, self.lSensorPos.y-self.r, self.r*2, self.r*2)
        pygame.draw.ellipse(surface=self.surface, color=RED, rect=_params)

        _params = (self.cSensorPos.x-self.r, self.cSensorPos.y-self.r, self.r*2, self.r*2)
        pygame.draw.ellipse(surface=self.surface, color=RED, rect=_params)
        '''




