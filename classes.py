import pygame as pg
import numpy as np

class ray:
    def __init__(self, pos = pg.math.Vector3(), dir = pg.math.Vector3()):
        self.dir = dir
        self.pos = pos

class rayTracingMaterial:
    def __init__(self, color = pg.math.Vector3()):
        self.color = color

class sphere:
    def __init__(self, pos = pg.math.Vector3(), radius = 0, rayTracingMaterial = rayTracingMaterial()):
        self.pos = pos
        self.radius = radius
        self.rayTracingMaterial = rayTracingMaterial

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