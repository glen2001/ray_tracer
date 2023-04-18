import pygame as pg
from classes import *

width, height = 500, 500

#top of window
backLeft = pg.math.Vector3(0, 0, 750)
backRight = pg.math.Vector3(width, 0, 750)
frontLeft = pg.math.Vector3(0, 0, -200)
frontRight = pg.math.Vector3(width, 0 , -200)

#bottom of window
backLeftB = pg.math.Vector3(0, height, 800)
backRightB = pg.math.Vector3(width, height, 800)
frontLeftB = pg.math.Vector3(0, height, -200)
frontRightB = pg.math.Vector3(width, height, -200)

p4 = pg.math.Vector3(width/3, height/2 - 90, 500)
p5 = pg.math.Vector3(width/2, height - 75, 600)
p6 = pg.math.Vector3(width/2 + 60, height/2, 450)

mainSphere = sphere(p4, 100)
mainSphere.rayTracingMaterial.color = pg.math.Vector3(88, 199, 102)
mainSphere.rayTracingMaterial.smoothness = 0.8

smallSphere = sphere(p6, 50)
smallSphere.rayTracingMaterial.color = pg.math.Vector3(120, 91, 217)
smallSphere.rayTracingMaterial.smoothness = 0.6

largeSphere = sphere(p5, 200)
largeSphere.rayTracingMaterial.color = pg.math.Vector3(176, 32, 70)
largeSphere.rayTracingMaterial.smoothness = 0.1

backWallMirror1 = triangle(backLeft, backLeftB, backRight)
backWallMirror1.rayTracingMaterial.color = pg.math.Vector3(173, 179, 174)
backWallMirror1.rayTracingMaterial.smoothness = .98

backWallMirror2 = triangle(backLeftB, backRightB, backRight)
backWallMirror2.rayTracingMaterial.color = pg.math.Vector3(173, 179, 174)
backWallMirror2.rayTracingMaterial.smoothness = .98

lightSource1 = triangle(backLeft, backRight, frontLeft)
lightSource1.rayTracingMaterial.emissionColor = pg.math.Vector3(1, 1, 1)
lightSource1.rayTracingMaterial.emissionStrength = 255

lightSource2 = triangle(frontLeft, frontRight, backRight)
lightSource2.rayTracingMaterial.emissionColor = pg.math.Vector3(1, 1, 1)
lightSource2.rayTracingMaterial.emissionStrength = 255


spheres = []
spheres.append(mainSphere)
spheres.append(largeSphere)
spheres.append(smallSphere)

triangles = []
triangles.append(lightSource1)
triangles.append(lightSource2)
triangles.append(backWallMirror1)
triangles.append(backWallMirror2)