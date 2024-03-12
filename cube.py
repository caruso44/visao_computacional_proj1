import numpy as np
from face import Face
import time

class Cube:
    def __init__(self, theta1, theta2, theta3, direc) -> None:
        self.dir = direc
        self.faces = []
        self.foco = np.array([0,1,0])
        self.faces.append(Face(theta1, theta2, theta3, [0, 1, 5, 4],-1, self.foco))
        self.faces.append(Face(theta1, theta2, theta3, [5, 7, 6, 4],-1, self.foco))
        self.faces.append(Face(theta1, theta2, theta3, [2, 3, 6, 7],1, self.foco))
        self.faces.append(Face(theta1, theta2, theta3, [0, 1, 2, 3],1, self.foco))
        self.faces.append(Face(theta1, theta2, theta3, [1, 3, 5, 7],-1, self.foco))
        self.faces.append(Face(theta1, theta2, theta3, [0, 2, 6, 4],1, self.foco))

    def rotate_faces(self):
        for face in self.faces:
            face.rotate_points()
    
    def clean_file(self):
        with open(self.dir, 'w') as arquivo:
            pass 

    def draw_frame(self, frame_rate):
        for face in self.faces:
            face.draw_line(self.dir)
        with open(self.dir, 'a') as arquivo:
            arquivo.write(f'delay\n' + str(1/frame_rate) + '\nclrscr\nend')

    def draw_frame_with_oclusion(self, frame_rate):
        for face in self.faces:
            if np.dot(np.array(face.normal), np.array((0,1,0))) > 0:
                face.draw_line(self.dir)
        with open(self.dir, 'a') as arquivo:
            arquivo.write(f'delay\n' + str(1/frame_rate) + '\nclrscr\nend')
    
    def draw_movie(self,frame_rate):
        tempo_limite = 3
        inicio = time.time()
        while time.time() - inicio < tempo_limite:
            self.draw_frame(frame_rate)
            self.rotate_faces()

    def draw_movie_with_oclusion(self,frame_rate):
        tempo_limite = 3
        inicio = time.time()
        while time.time() - inicio < tempo_limite:
            self.draw_frame_with_oclusion(frame_rate)
            self.rotate_faces()



cubo = Cube(0,1,0.5,'q4v3.txt')
cubo.clean_file()
cubo.rotate_faces()
cubo.draw_movie_with_oclusion(30)