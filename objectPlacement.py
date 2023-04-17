import pygame as pg
from classes import *

width, height = 600, 600

mainSphere = sphere(pg.math.Vector3(width/2, height/2, 600), 300)
mainSphere.rayTracingMaterial.color = pg.math.Vector3(209, 220, 237)
mainSphere.rayTracingMaterial.smoothness = .999

behindCameraSphere1 = sphere(pg.math.Vector3(width/2 + 600, height/2, -100), 600)
behindCameraSphere1.rayTracingMaterial.color = pg.math.Vector3(252, 186, 3)
behindCameraSphere1.rayTracingMaterial.smoothness = .98

behindCameraSphere2 = sphere(pg.math.Vector3(width/2 - 600, height/2, -600), 600)
behindCameraSphere2.rayTracingMaterial.color = pg.math.Vector3(167, 27, 209)
behindCameraSphere2.rayTracingMaterial.smoothness = .3

lightSource = sphere(pg.math.Vector3(width/2, -1500, 200), 1500)
lightSource.rayTracingMaterial.emissionStrength = 255
lightSource.rayTracingMaterial.emissionColor = pg.math.Vector3(1, 1, 1)
lightSource.rayTracingMaterial.color = pg.math.Vector3(0, 0, 0)

spheres = []
spheres.append(mainSphere)
spheres.append(lightSource)
spheres.append(behindCameraSphere1)
spheres.append(behindCameraSphere2)