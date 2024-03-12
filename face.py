import numpy as np
import math

class Face:
    def __init__(self, theta1, theta2, theta3, vertices, orientation, foco) -> None:
        self.vertices = []
        for vertice in vertices:
            self.vertices.append(self.get_coordinates(vertice))
        self.theta1 = (np.pi * theta1)/180
        self.theta2 = (np.pi * theta2)/180
        self.theta3 = (np.pi * theta3)/180
        self.create_rotation_matrix()
        self.normal = self.get_cross_product()
        self.normal *= orientation
        self.foco = foco

    def get_cross_product(self):
        vector1 = np.array(self.vertices[1]) - np.array(self.vertices[0])
        vector2 = np.array(self.vertices[2]) - np.array(self.vertices[0])
        produto_vetorial = np.cross(vector1, vector2)
        norma = np.linalg.norm(produto_vetorial)
        vetor_normalizado =  (produto_vetorial / norma)
        return vetor_normalizado

    def get_coordinates(self, n):
        binario = bin(n)[2:]
        binario_completo = binario.zfill(3) 
        coordenadas = [int(digito) for digito in binario_completo]
        for i in range (len(coordenadas)):
            coordenadas[i] /=2
        return coordenadas

    def create_rotation_matrix(self):
        self.M1 = [
        [math.cos(self.theta1), math.sin(self.theta1), 0],
        [-math.sin(self.theta1), math.cos(self.theta1), 0],
        [0,0,1]
        ]
        self.M2 = [
            [1,0,0],
            [0,math.cos(self.theta2), math.sin(self.theta2)],
            [0,-math.sin(self.theta2), math.cos(self.theta2)]
        ]
        self.M3 = [
            [math.cos(self.theta3), 0, math.sin(self.theta3)],
            [0,1,0],
            [-math.sin(self.theta3), 0, math.cos(self.theta3)]
        ]


    def draw_line(self, directoy):
        with open(directoy, 'a') as arquivo:
            for i in range(4):
                for j in range(i + 1, 4):
                    v1 = self.vertices[i]
                    v2  = self.vertices[j]
                    if(np.linalg.norm(np.array(v1) - np.array(v2)) < 0.6):
                        arquivo.write('line\n')
                        arquivo.write(f'{v1[0]} {v1[2]} {v2[0]} {v2[2]}\n')
    
    def rotate_points(self):
        vertices_rotated = []
        for i in range(4):
            aux = np.array(self.vertices[i])
            aux = np.dot(aux, self.M3)
            aux = np.dot(aux,self.M2)  
            aux = np.dot(aux,self.M1)
            vertices_rotated.append(aux.tolist())
        aux = np.array(self.normal)
        aux = np.dot(aux, self.M3)
        aux = np.dot(aux,self.M2)  
        aux = np.dot(aux,self.M1)
        self.normal = aux
        self.vertices = vertices_rotated
    

    def calculate_intersection(self, ponto):
        x1, y1, z1 = self.foco
        x2, y2, z2 = ponto
        
        delta_x = x2 - x1
        delta_y = y2 - y1
        delta_z = z2 - z1
        

        t = -y1 / delta_y
        
        x_intersecao = x1 + t * delta_x
        y_intersecao = y1 + t * delta_y
        z_intersecao = z1 + t * delta_z
        return x_intersecao, y_intersecao, z_intersecao

    def get_point_in_face(self):
        v1 = []
        for i in range(3):
            v1.append((self.vertices[0][i] + self.vertices[2][i])/2)
        return v1
    

    def draw_line_projective(self, directoy):
        with open(directoy, 'a') as arquivo:
            aux = 0
            for i in range(4):
                for j in range(4):
                    aux += 1
                    v1 = self.vertices[i]
                    v2  = self.vertices[j]
                    if(np.linalg.norm(np.array(v1) - np.array(v2)) < 0.7): 
                        v1 = self.calculate_intersection(v1)
                        v2 = self.calculate_intersection(v2)
                        arquivo.write('line\n')
                        arquivo.write(f'{v1[0]} {v1[2]} {v2[0]} {v2[2]}\n')