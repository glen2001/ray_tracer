import pygame as pg
from classes import *

width, height = 500, 500

#Cube Vertecies
CtopBackLeft = pg.math.Vector3(width/4, height/4, 400)
CtopBackRight = pg.math.Vector3(3*width/4, height/4, 600)
CtopFrontLeft = pg.math.Vector3(width/4, height/4, 200)
CtopFrontRight = pg.math.Vector3(3*width/4, height/4, 200)

CbottomBackLeft = pg.math.Vector3(width/4, 3*height/4, 400)
CbottomBackRight = pg.math.Vector3(3*width/4, 3*height/4, 600)
CbottomFrontLeft = pg.math.Vector3(width/4, 3*height/4, 200)
CbottomFrontRight = pg.math.Vector3(3*width/4, 3*height/4, 200)

#top of window
backLeftT = pg.math.Vector3(0, 0, 750)
backRightT = pg.math.Vector3(width, 0, 750)
frontLeftT = pg.math.Vector3(0, 0, -200)
frontRightT = pg.math.Vector3(width, 0 , -200)

#sphere points
mainSpherePos = pg.math.Vector3(400, height/2, 500)

plane1 = triangle(CtopBackLeft, CtopBackRight, CbottomBackLeft)
plane1.rayTracingMaterial.color = pg.math.Vector3(155, 155, 200)
plane1.rayTracingMaterial.smoothness = 0.998

plane2 = triangle(CtopBackRight, CbottomBackRight, CbottomBackLeft)
plane2.rayTracingMaterial.color = pg.math.Vector3(155, 155, 200)
plane2.rayTracingMaterial.smoothness = 0.998

mainSphere = sphere(mainSpherePos, 70)
mainSphere.rayTracingMaterial.color = pg.math.Vector3(250, 15, 200)
mainSphere.rayTracingMaterial.smoothness = .7

lightSource1 = triangle(backLeftT, backRightT, frontLeftT)
lightSource1.rayTracingMaterial.emissionColor = pg.math.Vector3(1, 1, 1)
lightSource1.rayTracingMaterial.emissionStrength = 255

lightSource2 = triangle(frontLeftT, frontRightT, backRightT)
lightSource2.rayTracingMaterial.emissionColor = pg.math.Vector3(1, 1, 1)
lightSource2.rayTracingMaterial.emissionStrength = 255


spheres = []
spheres.append(mainSphere)


triangles = []
triangles.append(lightSource1)
triangles.append(lightSource2)
triangles.append(plane1)
triangles.append(plane2)
