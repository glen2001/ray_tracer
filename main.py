import sys
import pygame as pg
import numpy as np
from classes import *
from pygame.locals import *
import time
from objectPlacement import *

t1 = time.time()
print('Rendering Scene...')

pg.init()
fps = 1
fpsClock = pg.time.Clock()

screen = pg.display.set_mode((width, height), pg.RESIZABLE)

iterations = 1
iterPixels = []

def allPixels():
  pixelColor = []
  for i in range(width):
    for j in range(height):
      RAY = ray(pg.math.Vector3(i, j, 0), pg.math.Vector3(0, 0, 1))
      pixelColor.append(Trace(RAY, spheres, 5))

  TWOD_PixelColor = nest_list(pixelColor, width, height)
  iterPixels.append(TWOD_PixelColor)

for k in range(iterations):
  print(f'Iteration: {k + 1}')
  allPixels()

avgPixels = []

print('Averaging Pixels...')

for i in range(width):
    for j in range(height):
      avgPixels.append(pg.math.Vector3())

avgPixels = nest_list(avgPixels, width, height)

for a in iterPixels:
  for i in range(width):
    for j in range(height):
      avgPixels[i][j] += a[i][j]

for i in range(width):
    for j in range(height):
      avgPixels[i][j] = avgPixels[i][j] / iterations

t2 = time.time()
print(f'Render Complete! \nComputation Time: {t2-t1:.2f} seconds.')

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
      color = avgPixels[i][j]
      screen.set_at((i,j), (color[0], color[1], color[2]))
        
