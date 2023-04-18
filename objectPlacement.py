import pygame as pg
from classes import *

width, height = 500, 500

p1 = pg.math.Vector3(100, 100, 400)
p2 = pg.math.Vector3(100, 400, 400)
p3 = pg.math.Vector3(400, 100, 200)

TRIANGLE = triangle(p1, p2, p3) 
TRIANGLE.rayTracingMaterial.color = pg.math.Vector3(100, 22, 22)
TRIANGLE.rayTracingMaterial.smoothness = .5

s1 = sphere(p1, 20)
s1.rayTracingMaterial.color = pg.math.Vector3(255, 1, 1)
s1.rayTracingMaterial.smoothness = .5

s2 = sphere(p2, 20)
s2.rayTracingMaterial.color = pg.math.Vector3(1, 1, 1)
s2.rayTracingMaterial.smoothness = .5

s3 = sphere(p3, 20)
s3.rayTracingMaterial.color = pg.math.Vector3(1, 1, 1)
s3.rayTracingMaterial.smoothness = .5

lightSource = sphere(pg.math.Vector3(width/2, -1501, 200), 1500)
lightSource.rayTracingMaterial.emissionStrength = 255
lightSource.rayTracingMaterial.emissionColor = pg.math.Vector3(1, 1, 1)
lightSource.rayTracingMaterial.color = pg.math.Vector3(0, 0, 0)

spheres = []
spheres.append(s1)
# spheres.append(s2)
# spheres.append(s3)
spheres.append(lightSource)
# spheres.append(behindCameraSphere1)
# spheres.append(behindCameraSphere2)

triangles = []
# triangles.append(TRIANGLE)