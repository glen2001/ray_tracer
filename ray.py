import pygame as pg

class ray:
    def __init__(self, pos, dir):
        self.dir = dir
        self.pos = pos

    def intersectingSphere(self, sphere):
