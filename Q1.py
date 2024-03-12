from cube import Cube

cubo = Cube(0,60,30,'q1.txt')
cubo.clean_file()
cubo.rotate_faces()
cubo.draw_frame(0.1)