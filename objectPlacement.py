import pygame as pg
from classes import *

width, height = 600, 600

SPHERE1 = sphere(pg.math.Vector3(width/2 + 120, height/2, 400), 100)
SPHERE1.rayTracingMaterial.color = pg.math.Vector3(99, 47, 196)
SPHERE1.rayTracingMaterial.smoothness = 0.65

SPHERE3 = sphere(pg.math.Vector3(width/2 - 120, height/2, 400), 100)
SPHERE3.rayTracingMaterial.color = pg.math.Vector3(196, 72, 47)
SPHERE3.rayTracingMaterial.smoothness = 0.65

SPHERE4 = sphere(pg.math.Vector3(width/2, height/2 + 700, 600), 600)
SPHERE4.rayTracingMaterial.color = pg.math.Vector3(189, 66, 111)
SPHERE4.rayTracingMaterial.smoothness = .7

SPHERE5 = sphere(pg.math.Vector3(width/3, height/4, 900), 200)
SPHERE5.rayTracingMaterial.color = pg.math.Vector3(47, 189, 196)
SPHERE5.rayTracingMaterial.smoothness = .2

SPHERE2 = sphere(pg.math.Vector3(width/2, -701, 400), 700)
SPHERE2.rayTracingMaterial.emissionStrength = 255
SPHERE2.rayTracingMaterial.emissionColor = pg.math.Vector3(1, 1, 1)
SPHERE2.rayTracingMaterial.color = pg.math.Vector3(0, 0, 0)

SPHERE6 = sphere(pg.math.Vector3(width/2, height/2 + 100, 300), 50)
SPHERE6.rayTracingMaterial.emissionStrength = 255
SPHERE6.rayTracingMaterial.emissionColor = pg.math.Vector3(1, 1, 1)
SPHERE6.rayTracingMaterial.color = pg.math.Vector3(0, 0, 0)

spheres = []
spheres.append(SPHERE1)
spheres.append(SPHERE2)
spheres.append(SPHERE3)
spheres.append(SPHERE4)
spheres.append(SPHERE5)
spheres.append(SPHERE6)