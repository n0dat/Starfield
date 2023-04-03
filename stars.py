# generate starts

from ursina import *

class Star():
    def __init__(self, x: int, y: int, z: int):
        self.e = Entity()
        self.e.color = color.white
        self.e.model = 'sphere'
        self.e.scale = (1, 1, 1)
        self.e.world_position = Vec3(x, y, z)
        
    def set_pos(self, x: int, y: int, z: int):
        self.e.world_position = Vec3(x, y, z)
    
    def get_pos(self):
        return (self.e.position)