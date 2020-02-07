import pygame
from vector3 import *

class Mesh:
    def __init__(self, name = "UnknownMesh"):
        self.name = name
        self.polygons = []

    def offset(self, v):
        new_polys = []
        for poly in self.polygons:
            new_poly = []
            for p in poly:
                new_poly.append(p + v)
            new_polys.append(new_poly)

        self.polygons = new_polys

    def render(self, screen, matrix, material):
        c = material.color.tuple3()        

        for poly in self.polygons:
            tpoly = []
            for v in poly:
                vout = v.to_np4()
                vout = vout @ matrix
                
                tpoly.append( ( screen.get_width() * 0.5 + vout[0] / vout[3], screen.get_height() * 0.5 - vout[1] / vout[3]) )

            
            pygame.draw.polygon(screen, (20,20,20), tpoly, material.fill)
            pygame.draw.polygon(screen, c, tpoly, material.line_width)


    @staticmethod
    def create_cube(size, mesh = None):
        if (mesh == None):
            mesh = Mesh("Cube1")

        Mesh.create_square(vector3( size[0] * 0.5, 0, 0), vector3(0, -size[1] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)
        Mesh.create_square(vector3(-size[0] * 0.5, 0, 0), vector3(0,  size[1] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)

        Mesh.create_square(vector3(0,  size[1] * 0.5, 0), vector3(size[0] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)
        Mesh.create_square(vector3(0, -size[1] * 0.5, 0), vector3(-size[0] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)

        Mesh.create_square(vector3(0, 0,  size[2] * 0.5), vector3(-size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), mesh)
        Mesh.create_square(vector3(0, 0, -size[2] * 0.5), vector3( size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), mesh)

        return mesh

    @staticmethod
    def create_Cube(size, mesh = None):
        if (mesh == None):
            mesh = Mesh("Cube2")
            
            Mesh.create_square(vector3(-size[0] * 0.5, 0, 0), vector3(0, 0, size[2] * 0.5), vector3(0, size[1] * 0.5, 0), mesh)
            Mesh.create_square(vector3(size[0] * 0.5, 0, 0), vector3(0, 0, size[2] * 0.5), vector3(0, size[1] * 0.5, 0), mesh)
            Mesh.create_square(vector3(0, 0, size[2] * 0.5), vector3(-size[0] * 0.5, 0, 0), vector3(0, size[1] * 0.5, 0), mesh)
            Mesh.create_square(vector3(0, 0, -size[2] * 0.5), vector3(size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), mesh)
            
            return mesh

    @staticmethod
    def create_square(origin, axis0, axis1, mesh):
        if (mesh == None):
            mesh = Mesh("Square")
        squares = []
        squares.append(origin + axis0 + axis1)
        squares.append(origin + axis0 - axis1)
        squares.append(origin - axis0 - axis1)
        squares.append(origin - axis0 + axis1)

        mesh.polygons.append(squares)
        '''
        p1 = (origin - axis0 + axis1)
        p2 = (origin - axis0 - axis1)
        p3 = (origin + axis0 + axis1)
        p4 = (origin + axis0 - axis1)
        
        squares.append(p1)
        squares.append(p2)
        squares.append(p3)
        squares.append(p4)
        
        v1 = (origin + axis0 + axis1) - (origin - axis0 + axis1)
        v2 = (origin + axis0 - axis1) - (origin + axis0 + axis1)
        
        cp = cross_product(v1,v2)
        cp.normalize()
        
        cameraDir = vector3 (-1,0,1)
        
        for sq in squares:
            if dot_product(cp, camereDir) > 0:
                mesh.polygons.append(squares)
                print(dot_product)
        for sq in squares:
            if dot_product(cp, cameraDir) < 0:
                mesh.polygons.append(squares)
'''
        return mesh
    
