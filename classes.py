import pygame as pg
import numpy as np
import random

class ray:
    def __init__(self, pos = pg.math.Vector3(), dir = pg.math.Vector3()):
        self.dir = dir
        self.pos = pos

class rayTracingMaterial:
    def __init__(self, color = pg.math.Vector3(), emissionColor = pg.math.Vector3(), emissionStrength = 0, smoothness = 0):
        self.color = color
        self.emissionColor = emissionColor
        self.emissionStrength = emissionStrength
        self.smoothness = smoothness

class sphere:
    def __init__(self, pos = pg.math.Vector3(), radius = 0):
        self.pos = pos
        self.radius = radius
        self.rayTracingMaterial = rayTracingMaterial()

class hitInfo:
    def __init__(self, didHit = False, hitPos = None, dist = 0, normal = None, rayTracingMaterial = rayTracingMaterial()):
        self.didHit = didHit
        self.hitPos = hitPos
        self.dist = dist
        self.normal = normal
        self.rayTracingMaterial = rayTracingMaterial

def RaySphere(ray = ray(), sphereCenter = pg.math.Vector3(), sphereRadius = 0):
    HIT_INFO = hitInfo()
    offsetRayOrigin = ray.pos - sphereCenter

    a = pg.math.Vector3.dot(ray.dir, ray.dir)
    b = 2 * pg.math.Vector3.dot(offsetRayOrigin, ray.dir)
    c = pg.math.Vector3.dot(offsetRayOrigin, offsetRayOrigin) - sphereRadius * sphereRadius

    discriminant = b * b - 4 * a * c

    if (discriminant >= 0):
        dst = (-b - np.sqrt(discriminant)) / (2 * a)

        if (dst >= 0):
            HIT_INFO.didHit = True
            HIT_INFO.dist = dst
            HIT_INFO.hitPos = ray.pos + ray.dir * dst
            HIT_INFO.normal = pg.math.Vector3.normalize(HIT_INFO.hitPos - sphereCenter)

    return HIT_INFO

def CalculateRayCollision(ray = ray(), spheres = []):
    clostestHit = hitInfo()
    clostestHit.dist = np.inf

    for i in spheres:
        SPHERE = i
        HIT_INFO = RaySphere(ray, SPHERE.pos, SPHERE.radius)

        if (HIT_INFO.didHit and HIT_INFO.dist < clostestHit.dist):
            clostestHit = HIT_INFO
            clostestHit.rayTracingMaterial = SPHERE.rayTracingMaterial

    return clostestHit

def RandomNormalVec(normal = pg.math.Vector3()):
    dir = pg.math.Vector3(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
    dir.normalize()
    dot = pg.math.Vector3.dot(normal, dir)
    if dot < 0:
        dir = -dir

    return dir

def Trace(ray = ray(), spheres = [], maxBounceCount = 1):
    incomingLight = pg.math.Vector3()
    rayColor = pg.math.Vector3(1, 1, 1)

    for i in range(maxBounceCount):
        HIT_INFO = CalculateRayCollision(ray, spheres)
        material = HIT_INFO.rayTracingMaterial
        if HIT_INFO.didHit:
            ray.pos = HIT_INFO.hitPos
            diffused = RandomNormalVec(HIT_INFO.normal)
            specular = pg.math.Vector3.reflect(ray.dir, HIT_INFO.normal)
            ray.dir = pg.math.Vector3.lerp(diffused, specular, material.smoothness)

            emittedLight = material.emissionColor * material.emissionStrength
            incomingLight += emittedLight.elementwise() * rayColor
            rayColor = (rayColor.elementwise() * material.color) / 255
        else:
            incomingLight += pg.math.Vector3(53, 174, 240).elementwise() * rayColor
            break

    incomingLight[0] = int(incomingLight[0])
    incomingLight[1] = int(incomingLight[1])
    incomingLight[2] = int(incomingLight[2])
        
    return incomingLight

def nest_list(list1,rows, columns):    
        result=[]               
        start = 0
        end = columns
        for i in range(rows): 
            result.append(list1[start:end])
            start +=columns
            end += columns
        return result
