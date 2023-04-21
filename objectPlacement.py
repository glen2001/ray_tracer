import pygame as pg
from classes import *

#This file is used to place objects in the scene, as well as specify the rayTracingMaterial properties of each object

width, height = 600, 600

#Cube Vertecies
CtopBackLeft = pg.math.Vector3(0, 0, 500)
CtopBackRight = pg.math.Vector3(width, 0, 500)
CtopFrontLeft = pg.math.Vector3(0, 0, -200)
CtopFrontRight = pg.math.Vector3(width, 0, -200)

CbottomBackLeft = pg.math.Vector3(0, height, 500)
CbottomBackRight = pg.math.Vector3(width, height, 500)
CbottomFrontLeft = pg.math.Vector3(0, height, -200)
CbottomFrontRight = pg.math.Vector3(width, height, -200)


#sphere points
mainSpherePos = pg.math.Vector3(width/2, height/2 + 200, 200)
smallSpherePos = pg.math.Vector3(3*width/4 + 50, height/2 + 80, 200)
lightSpherePos = pg.math.Vector3(width/2, height/2 - 100, 300)
mediumSpherePos = pg.math.Vector3(width/2 - 200, height/3, 300)
mediumSpherePos2 = pg.math.Vector3(3*width/4 + 50, height/2 + 220, 200)

plane1 = triangle(CtopBackRight, CtopBackLeft, CbottomBackLeft)
plane1.rayTracingMaterial.color = pg.math.Vector3(250, 244, 227)
plane1.rayTracingMaterial.smoothness = 0.2

plane2 = triangle(CbottomBackRight, CtopBackRight, CbottomBackLeft)
plane2.rayTracingMaterial.color = pg.math.Vector3(250, 244, 227)
plane2.rayTracingMaterial.smoothness = 0.2

plane3 = triangle(CbottomBackRight, CbottomBackLeft, CbottomFrontLeft)
plane3.rayTracingMaterial.color = pg.math.Vector3(250, 244, 227)
plane3.rayTracingMaterial.smoothness = 0.2

plane4 = triangle(CbottomFrontRight, CbottomBackRight, CbottomFrontLeft)
plane4.rayTracingMaterial.color = pg.math.Vector3(250, 244, 227)
plane4.rayTracingMaterial.smoothness = 0.2

plane5 = triangle(CbottomBackLeft, CtopBackLeft, CtopFrontLeft)
plane5.rayTracingMaterial.color = pg.math.Vector3(250, 244, 227)
plane5.rayTracingMaterial.smoothness = 0.2

plane6 = triangle(CbottomFrontLeft, CbottomBackLeft, CtopFrontLeft)
plane6.rayTracingMaterial.color = pg.math.Vector3(250, 244, 227)
plane6.rayTracingMaterial.smoothness = 0.2

plane7 = triangle(CtopBackRight, CbottomBackRight, CtopFrontRight)
plane7.rayTracingMaterial.color = pg.math.Vector3(250, 244, 227)
plane7.rayTracingMaterial.smoothness = 0.2

plane8 = triangle(CbottomBackRight, CbottomFrontRight, CtopFrontRight)
plane8.rayTracingMaterial.color = pg.math.Vector3(250, 244, 227)
plane8.rayTracingMaterial.smoothness = 0.2

plane9 = triangle(CbottomFrontLeft, CtopFrontLeft, CtopFrontRight)
plane9.rayTracingMaterial.color = pg.math.Vector3(250, 244, 227)
plane9.rayTracingMaterial.smoothness = 0.2

plane10 = triangle(CbottomFrontLeft, CtopFrontRight, CbottomFrontRight)
plane10.rayTracingMaterial.color = pg.math.Vector3(250, 244, 227)
plane10.rayTracingMaterial.smoothness = 0.2

lightSource1 = triangle(CtopBackLeft, CtopBackRight, CtopFrontLeft)
lightSource1.rayTracingMaterial.color = pg.math.Vector3(250, 244, 227)
lightSource1.rayTracingMaterial.smoothness = 0.2
# lightSource1.rayTracingMaterial.emissionColor = pg.math.Vector3(1, 1, 1)
# lightSource1.rayTracingMaterial.emissionStrength = 255

lightSource2 = triangle(CtopFrontRight, CtopFrontLeft, CtopBackRight)
lightSource2.rayTracingMaterial.color = pg.math.Vector3(250, 244, 227)
lightSource2.rayTracingMaterial.smoothness = 0.2
# lightSource2.rayTracingMaterial.emissionColor = pg.math.Vector3(1, 1, 1)
# lightSource2.rayTracingMaterial.emissionStrength = 255

mainSphere = sphere(mainSpherePos, 100)
mainSphere.rayTracingMaterial.color = pg.math.Vector3(204, 218, 240)
mainSphere.rayTracingMaterial.smoothness = .98

smallSphere = sphere(smallSpherePos, 60)
smallSphere.rayTracingMaterial.color = pg.math.Vector3(255, 38, 45)
smallSphere.rayTracingMaterial.smoothness = .5

lightSphere = sphere(lightSpherePos, 100)
lightSphere.rayTracingMaterial.emissionColor = pg.math.Vector3(1, 1, 1)
lightSphere.rayTracingMaterial.emissionStrength = 255

mediumSphere = sphere(mediumSpherePos, 80)
mediumSphere.rayTracingMaterial.color = pg.math.Vector3(240, 110, 235)
mediumSphere.rayTracingMaterial.smoothness = 0

blueSphere = sphere(mediumSpherePos2, 80)
blueSphere.rayTracingMaterial.color = pg.math.Vector3(12, 71, 235)
blueSphere.rayTracingMaterial.smoothness = 0.3


spheres = []
spheres.append(mainSphere)
spheres.append(smallSphere)
spheres.append(lightSphere)
spheres.append(mediumSphere)
spheres.append(blueSphere)


triangles = []
triangles.append(lightSource1)
triangles.append(lightSource2)
triangles.append(plane1)
triangles.append(plane2)
triangles.append(plane3)
triangles.append(plane4)
triangles.append(plane5)
triangles.append(plane6)
triangles.append(plane7)
triangles.append(plane8)
triangles.append(plane9)
triangles.append(plane10)