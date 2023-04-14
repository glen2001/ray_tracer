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
 
width, height = 800, 800
screen = pg.display.set_mode((width, height), pg.RESIZABLE)

SPHERE1 = sphere(pg.math.Vector3(400, height/2, 400), 100)
SPHERE1.rayTracingMaterial.color = pg.math.Vector3(255, 0, 0)

SPHERE2 = sphere(pg.math.Vector3(0, 0, 200), 200)
SPHERE2.rayTracingMaterial.emissionStrength = 1
SPHERE2.rayTracingMaterial.emissionColor = pg.math.Vector3(255, 255, 255)
SPHERE2.rayTracingMaterial.color = pg.math.Vector3(0, 0, 0)

SPHERE3 = sphere(pg.math.Vector3(200, height/2, 200), 50)
SPHERE3.rayTracingMaterial.color = pg.math.Vector3(0, 0, 255)

spheres = []
spheres.append(SPHERE1)
spheres.append(SPHERE2)
spheres.append(SPHERE3)


pixelColor = []

for i in range(width):
  for j in range(height):
    RAY = ray(pg.math.Vector3(i, j, 0), pg.math.Vector3(0, 0, 1))
    pixelColor.append(Trace(RAY, spheres, 10))

#pixelColor = np.asarray(pixelColor)
#TWOD_PixelColor = pixelColor.reshape(width, height)

TWOD_PixelColor = nest_list(pixelColor, width, height)


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
      color = TWOD_PixelColor[i][j]
      screen.set_at((i,j), (color[0], color[1], color[2]))
        
