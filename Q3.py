from cube_projective import CubeProjective


cubo = CubeProjective(0,30,15,'q3_sem_oclusao.txt')
cubo.clean_file()
cubo.rotate_faces()
cubo.draw_frame(0.1)


cubo = CubeProjective(0,30,15,'q3_com_oclusao.txt')
cubo.clean_file()
cubo.rotate_faces()
cubo.draw_frame_with_oclusion(0.1)