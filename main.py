from estudiante import Estudiante
from curso import Curso

est_uno = Estudiante(292, "Arturo Melchor Ponce de León", 19)
est_dos = Estudiante(203, "Violeta Vázquez Riveira", 23)
est_tres = Estudiante(167, "Marco Castillo De Palomares", 21)

curso_uno = Curso("Mecanismos", 9092, "Carolina Mares Yamada")
curso_dos = Curso("Guitarra española", 1001, "Xo Zhua Palacios")
curso_tres = Curso("Teoría de personalidades", 2053, "Wener Schulz Black")
curso_cuatro = Curso("Química orgánica", 6548, "Vartán Campbell Nkosi")

est_uno.agregar_curso(curso_dos)
est_uno.agregar_curso(curso_tres)
est_dos.agregar_curso(curso_cuatro)
est_dos.agregar_curso(curso_dos)
est_tres.agregar_curso(curso_cuatro)
est_tres.agregar_curso(curso_uno)

est_uno.mostrar_info()
est_dos.mostrar_info()
est_tres.mostrar_info()

curso_uno.mostrar_info_curso()
curso_dos.mostrar_info_curso()
curso_tres.mostrar_info_curso()
curso_cuatro.mostrar_info_curso()