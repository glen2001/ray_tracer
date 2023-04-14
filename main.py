import sys
import pygame as pg
import numpy as np
from classes import *
from pygame.locals import *


pg.init()
fps = 60
fpsClock = pg.time.Clock()
 
width, height = 640, 480
screen = pg.display.set_mode((width, height), pg.RESIZABLE)

SPHERE = sphere(pg.math.Vector3(width/2, height/2, 50), 15)

pixelColor = []

for i in range(width):
  for j in range(height):
    RAY = ray(pg.math.Vector3(i, j, 0), pg.math.Vector3(0, 0, 1))
    pixelColor.append(RaySphere(RAY, SPHERE.pos, SPHERE.radius).didHit)

pixelColor = np.asarray(pixelColor)
newPixelColor = pixelColor.reshape(width, height)


# Game loop.
while True:  
  for event in pg.event.get():
    if event.type == QUIT:
      pg.quit()
      sys.exit()
  


  pg.display.update()
  fpsClock.tick(fps)
  screen.fill('black')

  for i in range(width):
    for j in range(height):
      if newPixelColor[i][j]:
        screen.set_at((i,j), 'white')
