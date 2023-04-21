import sys
import pygame as pg
import numpy as np
from classes import *
from pygame.locals import *
import time
from objectPlacement import *

avgPixels = []
for i in range(width):
    for j in range(height):
      avgPixels.append(pg.math.Vector3())

avgPixels = nest_list(avgPixels, width, height)



pg.init()
fps = 1000
fpsClock = pg.time.Clock()
screen = pg.display.set_mode((width, height), pg.RESIZABLE)


# Game loop.

i = 0
j = 0
iterations = 1
fov_factor = 0.001
while True:  
  for event in pg.event.get():
    if event.type == QUIT:
      pg.quit()
      sys.exit()
  

  pg.display.update()
#   fpsClock.tick(fps)
#   screen.fill('black')
  
  RAY = ray(pg.math.Vector3(i, j, 0), pg.math.Vector3((i-width/2) * fov_factor, (j-height/2) * fov_factor, 1).normalize())
  color =  Trace(RAY, spheres, triangles, 3)
  
#   avgPixels[i][j] = avgPixels[i][j] / iterations


  screen.set_at((i,j), (color[0], color[1], color[2]))

  i += 1

  if i == width:
    i = 0
    j += 1
  if j == height:
    iterations += 1
    j = 0
  
  