from sqlmodel import SQLModel, Field

class MoviesModel(SQLModel, table=True):
    __tablename__= "Movies"
    
    id: int = Field(primary_key=True)
    nombre_pelicula: str
    año_estreno: str
    duracion: str
    director: str
    clasificacion: str
    genero: str