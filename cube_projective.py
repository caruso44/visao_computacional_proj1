import numpy as np
from cube import Cube
import time


class CubeProjective(Cube):
    def __init__(self, theta1, theta2, theta3, direc) -> None:
        super().__init__(theta1, theta2, theta3, direc)

    
    def draw_frame(self, frame_rate):
        for face in self.faces:
            face.draw_line_projective(self.dir)
        with open(self.dir, 'a') as arquivo:
            arquivo.write(f'delay\n' + str(1/frame_rate) + '\nclrscr\nend')
    
    def draw_frame_with_oclusion(self, frame_rate):
        for face in self.faces:
            if (np.dot(np.array(face.normal), np.array(self.foco) - np.array(face.get_point_in_face())) > 0):
                face.draw_line_projective(self.dir)
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
