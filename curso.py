
class Curso:
    nombre_curso = ""
    codigo_curso = 0
    instructor = ""
    
    def __init__(self, nombre_curso, codigo_curso, instructor):
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso
        self.instructor = instructor
    
    def mostrar_info_curso(self):
        print("\n______ Información del curso ______\n")
        print("Nombre del curso: ", self.nombre_curso)
        print("Código del curso: ", self.codigo_curso)
        print("Maestro: ", self.instructor)
        
    