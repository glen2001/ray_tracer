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

SPHERE1 = sphere(pg.math.Vector3(width/2, height/2, 50), 15)
SPHERE1.rayTracingMaterial.color = pg.math.Vector3(255, 0, 0)

SPHERE2 = sphere(pg.math.Vector3(width/3, height/3, 50), 25)
SPHERE2.rayTracingMaterial.color = pg.math.Vector3(255, 255, 0)

spheres = []
spheres.append(SPHERE1)
spheres.append(SPHERE2)

print(spheres[0].rayTracingMaterial.color)

pixelColor = []

for i in range(width):
  for j in range(height):
    RAY = ray(pg.math.Vector3(i, j, 0), pg.math.Vector3(0, 0, 1))
    pixelColor.append(CalculateRayCollision(RAY, spheres))

pixelColor = np.asarray(pixelColor)
TWOD_PixelColor = pixelColor.reshape(width, height)


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
      color = TWOD_PixelColor[i][j].rayTracingMaterial.color
      screen.set_at((i,j), (color[0], color[1], color[2]))
        
