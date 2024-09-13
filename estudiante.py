class Estudiante:
    id_estudiante = 0
    nombre = ""
    edad = 0
    cursos = []
    
    def __init__(self, id_estudiante, nombre, edad):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.edad = edad
        self.cursos = []
        
    def agregar_curso(self, curso):
        self.cursos.append(curso)     
    
    def mostrar_info(self):
        print("\n_______Estudiante inscrito_________\n")
        print("ID: ", self.id_estudiante)
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("\n## Cursos a los que está inscrito el estudiante ## ")
        # print("Cursos: ", self.cursos)
        
        for curso in self.cursos:
            print("Materia:",curso.nombre_curso)