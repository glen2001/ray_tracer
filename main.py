import sys
import pygame as pg
import numpy as np
from classes import *
from pygame.locals import *
import time
from objectPlacement import *

#This file is the used to average pixels colors over a number of iterations, as well as display the scene

#record time before calulations
t1 = time.time()
print('Rendering Scene...')


#initialize simulation values
iterations = 20
bounces = 6

#initialize avgPixels with vectors of length 0, then nest into 2d array. Note that color is stored in the form of a Vector3, mainly for convience
avgPixels = []
for i in range(width):
    for j in range(height):
      avgPixels.append(pg.math.Vector3())

avgPixels = nest_list(avgPixels, width, height)

#calculate pixel color values, then add them to avgPixels. Do this for number of iterations
for k in range(iterations):
  print(f'Iteration: {k + 1}')
  pix = allPixels(width, height, bounces, spheres, triangles)

  for i in range(width):
    for j in range(height):
      avgPixels[i][j] += pix[i][j]

  if k == 0:
    tEstimated = time.time()
    print(f'Estimated Render Time: {(((tEstimated-t1) / 60) * (iterations)):.2f} minutes')
    
#normalize values stored in avgPixles. This helps reduce noise with more iterations
for i in range(width):
    for j in range(height):
      avgPixels[i][j] = avgPixels[i][j] / iterations

#record time after calculations. Prints out time spent on calculation
t2 = time.time()
print(f'Render Complete! \nComputation Time: {(t2-t1) / 60:.2f} minutes.')


#initialize pyGame window to display pixels
pg.init()
fps = 60
fpsClock = pg.time.Clock()
screen = pg.display.set_mode((width, height), pg.RESIZABLE)

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
        
