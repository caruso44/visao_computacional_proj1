from cube import Cube

cubo = Cube(0,60,30,'q2.txt')
cubo.clean_file()
cubo.rotate_faces()
cubo.draw_frame_with_oclusion(0.1)