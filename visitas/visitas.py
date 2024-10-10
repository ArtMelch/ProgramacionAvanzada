from guia.guia import Guia
from visitante.visitante import Visitante
from typing import List

class Visita:
    guia: Guia
    visitantes: List[Visitante]=[]
    
    def __init__(self,guia:Guia,visitantes: List[Visitante]):
        self.visitantes = visitantes
        self.guia = guia
        
    