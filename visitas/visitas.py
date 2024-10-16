from guia.guia import Guia
from visitante.visitante import Visitante
from typing import List

class Visita:
    id = str
    guia: Guia
    visitantes: List[Visitante] = []
    
    def __init__(self, id:str, guia:Guia, visitantes: List[Visitante]):
        self.id = id
        self.visitantes = visitantes
        self.guia = guia
        
    def mostrar_info_visitas(self):
        info = f"ID: {self.id} \nGuía encargado: {self.guia.nombre}"
        print(info)
        print("\n--VISITANTES--")
        for visitante in self.visitantes:
            print(f"\nNombre: {visitante.nombre} {visitante.apellidos} \nID: {visitante.id_visitante}")
        