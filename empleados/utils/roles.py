from enum import Enum

class Rol(Enum):
    #tipo de animal
    ACUATICO = "Acuatico"
    TERRESTRE = "Terrestre"
    AEREOS = "Aereos"
    
    #tipo de alimentación
    CARNIVORO = "Carnivoro"
    HERBIVORO = "Herbivoro"
    
    #empleados
    DIRECTOR = "Director"
    GUIA = "Guia"
    VETERINARIO = "Veterinario"
    MANTENIMIENTO = "Mantenimiento"
    
    #visitantes
    VISITANTE = "Visitante"
    # ADULTO = "Adulto"
    # INFANTE = "Infante"