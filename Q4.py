from cube import Cube
from cube_projective import CubeProjective


cubo = Cube(0,1,0.5,'q4_sem_projecao_sem_oclusao.txt')
cubo.clean_file()
cubo.rotate_faces()
cubo.draw_movie(60)


cubo = Cube(0,1,0.5,'q4_sem_projecao_com_oclusao.txt')
cubo.clean_file()
cubo.rotate_faces()
cubo.draw_movie_with_oclusion(60)


cubo = CubeProjective(0,1,0.5,'q4_com_projecao_sem_oclusao.txt')
cubo.clean_file()
cubo.rotate_faces()
cubo.draw_movie(60)


cubo = CubeProjective(0,1,0.5,'q4_com_projecao_com_oclusao.txt')
cubo.clean_file()
cubo.rotate_faces()
cubo.draw_movie_with_oclusion(60)