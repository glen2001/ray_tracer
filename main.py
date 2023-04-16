import sys
import pygame as pg
import numpy as np
from classes import *
from pygame.locals import *
import time

t1 = time.time()
print('Rendering Scene...')

pg.init()
fps = 60
fpsClock = pg.time.Clock()
 
width, height = 500, 500
screen = pg.display.set_mode((width, height), pg.RESIZABLE)

SPHERE1 = sphere(pg.math.Vector3(width/2 + 100, height/2, 400), 100)
SPHERE1.rayTracingMaterial.color = pg.math.Vector3(66, 135, 245)

SPHERE3 = sphere(pg.math.Vector3(width/2 - 100, height/2, 400), 100)
SPHERE3.rayTracingMaterial.color = pg.math.Vector3(161, 219, 156)

SPHERE4 = sphere(pg.math.Vector3(width/2, height/2 + 600, 600), 600)
SPHERE4.rayTracingMaterial.color = pg.math.Vector3(189, 66, 111)

SPHERE5 = sphere(pg.math.Vector3(width/2 + 250, height/2 + 50, 300), 50)
SPHERE5.rayTracingMaterial.color = pg.math.Vector3(255, 0, 255)

SPHERE2 = sphere(pg.math.Vector3(width/2 , -600, 300), 600)
SPHERE2.rayTracingMaterial.emissionStrength = 1
SPHERE2.rayTracingMaterial.emissionColor = pg.math.Vector3(1, 1, 1)
SPHERE2.rayTracingMaterial.color = pg.math.Vector3(0, 0, 0)

spheres = []
spheres.append(SPHERE1)
spheres.append(SPHERE2)
#spheres.append(SPHERE3)
spheres.append(SPHERE4)
# spheres.append(SPHERE5)

iterations = 10
iterPixels = []

for k in range(iterations):
  print(f'Iteration: {k + 1}')
  pixelColor = []
  for i in range(width):
    for j in range(height):
      RAY = ray(pg.math.Vector3(i, j, 0), pg.math.Vector3(0, 0, 1))
      pixelColor.append(Trace(RAY, spheres, 4))

  TWOD_PixelColor = nest_list(pixelColor, width, height)
  iterPixels.append(TWOD_PixelColor)

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
        
