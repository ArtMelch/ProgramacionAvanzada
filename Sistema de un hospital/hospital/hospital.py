from typing import List
from paciente.paciente import Paciente
from medico.medico import Medico
from consulta.consulta import Consulta

class Hospital:
    pacientes : List[Paciente] = []
    medicos : List[Medico] = []
    consultas : List[Consulta] = []
    
    def registrar_consulta(self, id_paciente, id_medico):
        if not self.validar_cantidad_usuarios():
            return
        print("\n\tValidación exitosa")
        
        if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico) == False:
            print("No se puede registrar la consulta, no existe el médico o el paciente")
            return
        print("\n\tContinuar con el registro")
        
        
        
    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)    
        
        
    def registrar_medico(self, medico):
        self.medicos.append(medico)
   
    def mostrar_medicos(self):
        print("\n_____Médicos en el sistema____")
        for medico in self.medicos:
            medico.mostrar_info_medico()
        
    def mostrar_pacientes(self):
        print("\n_____Pacientes en el sistema____")
        for paciente in self.pacientes:
           paciente.mostrar_info_paciente()
            
        
    def validar_existencia_paciente(self,id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
        return False 
            
            
    def validar_existencia_medico(self,id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
            
        return False
    
    
    def validar_cantidad_usuarios(self):
        if len(self.pacientes) == 0:
            print("\nNo puedes registrar una consulta, no existen pacientes")
            return False
        
        
        if len(self.medicos) == 0:
            print("\nNo puedes registrar una consulta, no existen medicos")
            return False
        
        return True
    
    
            #print("Paciente mayore de edad: ", paciente.paciente_mayor_edad)
    # def validar_mayoria_edad_paciente(self, paciente):
    #     for paciente in self.pacientes:
    #         if (2024 - 2010)  >= 18:
    #             self.pacientes_adultos.append(paciente)
    #             paciente.mostrar_info_adulto()
    #         else:
    #             self.pacientes_ninos.append(paciente)
    #             print("\n------------- Paciente menores de edad ---------")
    #             paciente.mostrar_info_nino()
    
    
    def mostrar_pacientes_adultos(self):
        print("\n/////// Pacientes mayores de edad ///////")
        for paciente in self.pacientes:
            if ( 2024 - paciente.ano_nacimiento) >= 18:
                paciente.mostrar_info_paciente()
        

    def mostrar_pacientes_ninos(self):
        print("\n//////// Pacientes menores de edad ////////")
        for paciente in self.pacientes:
            if(2024 - paciente.ano_nacimiento) < 18:
                paciente.mostrar_info_paciente()
            
            
    def eliminar_medico(self, id_doc_eliminar):
        for medico in self.medicos:
            if medico.id == id_doc_eliminar:
                self.medicos.remove(medico)
                print(f"\nSe elimino al medico con el ID: {id_doc_eliminar} \n")


    def eliminar_paciente(self, id_pac_eliminar):
        for paciente in self.pacientes:
            if paciente.id == id_pac_eliminar:
                self.pacientes.remove(paciente)
                print(f"\nSe elimino al paciente con el ID: {id_pac_eliminar} \n")