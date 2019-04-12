import bpy
import bmesh
from mathutils import Vector

 

class Branch:
    def __init__(self, radius1, radius2, height, mat):
        self.radius1 = radius1
        self.radius2 = radius2
        self.height = height
        self.mat = mat
        self.bm = bmesh.new()
        #self.me = bpy.data.meshes.new("Branch")
        
        
    def add_mesh(self):
        bmesh.ops.create_cone(
            self.bm,
            cap_ends = True,
            diameter1 = self.radius1,
            diameter2 = self.radius2,
            depth = self.height,
            matrix = self.mat,
            segments = 32.0)
                
        #self.bm.to_mesh(self.me)
        #self.bm.free()

#    def add_mesh(self):
#            bpy.ops.primitive_cone_add(
#                radius1 = self.radius1,
#                radius2 = self.radius2,
#                depth = self.height,
#                location = self.position,
#                rotation = self.orientation)  
            
    

class State:
    def __init__(self, pos, pitch_dir, yaw_dir, roll_dir, mat_rot, radius1, radius2, segments):
   
        self.position = pos
        self.pitch_dir = pitch_dir
        self.yaw_dir = yaw_dir
        self.roll_dir = roll_dir
        self.mat_rot = mat_rot
        self.radius1 = radius1
        self.radius2 = radius2
        self.segments = segments
        


        
    



