import pygame as pg
from classes import *

#This file is used to place objects in the scene, as well as specify the rayTracingMaterial properties of each object

width, height = 700, 700

#Cube Vertecies
CtopBackLeft = pg.math.Vector3(0, 0, 600)
CtopBackRight = pg.math.Vector3(width, 0, 600)
CtopFrontLeft = pg.math.Vector3(0, 0, 200)
CtopFrontRight = pg.math.Vector3(width, 0, 200)

CbottomBackLeft = pg.math.Vector3(0, height, 650)
CbottomBackRight = pg.math.Vector3(width, height, 650)
CbottomFrontLeft = pg.math.Vector3(0, height, 200)
CbottomFrontRight = pg.math.Vector3(width, height, 200)

#top of window
backLeftT = pg.math.Vector3(-300, 0, 750)
backRightT = pg.math.Vector3(width + 300, 0, 750)
frontLeftT = pg.math.Vector3(-300, 0, -200)
frontRightT = pg.math.Vector3(width + 300, 0 , -200)

#sphere points
mainSpherePos = pg.math.Vector3(width/2, height/2 + 200, 400)
smallSpherePos = pg.math.Vector3(width/2, height/2, 400)

plane1 = triangle(CtopBackLeft, CtopBackRight, CbottomBackLeft)
plane1.rayTracingMaterial.color = pg.math.Vector3(155, 155, 200)
plane1.rayTracingMaterial.smoothness = 0.98

plane2 = triangle(CtopBackRight, CbottomBackRight, CbottomBackLeft)
plane2.rayTracingMaterial.color = pg.math.Vector3(155, 155, 200)
plane2.rayTracingMaterial.smoothness = 0.98

plane3 = triangle(CbottomBackRight, CbottomBackLeft, CbottomFrontLeft)
plane3.rayTracingMaterial.color = pg.math.Vector3(240, 96, 185)
plane3.rayTracingMaterial.smoothness = 0

plane4 = triangle(CbottomFrontRight, CbottomBackRight, CbottomFrontLeft)
plane4.rayTracingMaterial.color = pg.math.Vector3(240, 96, 185)
plane4.rayTracingMaterial.smoothness = 0

plane5 = triangle(CbottomBackLeft, CtopBackLeft, CtopFrontLeft)
plane5.rayTracingMaterial.color = pg.math.Vector3(155, 155, 200)
plane5.rayTracingMaterial.smoothness = 0.998

plane6 = triangle(CbottomBackLeft, CbottomFrontLeft, CtopFrontLeft)
plane6.rayTracingMaterial.color = pg.math.Vector3(155, 155, 200)
plane6.rayTracingMaterial.smoothness = 0.998

lightSource1 = triangle(backLeftT, backRightT, frontLeftT)
lightSource1.rayTracingMaterial.emissionColor = pg.math.Vector3(1, 1, 1)
lightSource1.rayTracingMaterial.emissionStrength = 255

lightSource2 = triangle(frontLeftT, frontRightT, backRightT)
lightSource2.rayTracingMaterial.emissionColor = pg.math.Vector3(1, 1, 1)
lightSource2.rayTracingMaterial.emissionStrength = 255

mainSphere = sphere(mainSpherePos, 100)
mainSphere.rayTracingMaterial.color = pg.math.Vector3(3, 252, 115)
mainSphere.rayTracingMaterial.smoothness = .95

smallSphere = sphere(smallSpherePos, 35)
smallSphere.rayTracingMaterial.color = pg.math.Vector3(255, 38, 45)
smallSphere.rayTracingMaterial.smoothness = .5

spheres = []
spheres.append(mainSphere)
spheres.append(smallSphere)


triangles = []
triangles.append(lightSource1)
triangles.append(lightSource2)
triangles.append(plane1)
triangles.append(plane2)
triangles.append(plane3)
triangles.append(plane4)
triangles.append(plane5)
triangles.append(plane6)
