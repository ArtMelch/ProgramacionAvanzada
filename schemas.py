from pydantic import BaseModel

class MovieSchemac(BaseModel):
    nombre_pelicula: str
    año_estreno: int
    duracion: str
    director: str
    clasificacion: str
    genero: str