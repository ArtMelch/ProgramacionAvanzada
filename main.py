from sqlmodel import select
from fastapi import FastAPI, HTTPException, status
from schemas import MovieSchemac
from models import MoviesModel
from random import randint
from database import create_db_and_tables,SessionDep

app = FastAPI()

create_db_and_tables()

@app.post("/movies")
async def create_movie(movie_data:MovieSchemac, database:SessionDep):
    movie= MoviesModel(nombre_pelicula=movie_data.nombre_pelicula, año_estreno=movie_data.año_estreno, duracion=movie_data.duracion, director=movie_data.director, clasificacion=movie_data.clasificacion, genero=movie_data.genero)
    
    database.add(movie)
    database.commit()
    database.refresh(movie)
    return movie

@app.get("/movies")
async def get_movies(database: SessionDep):
    statement = select(MoviesModel)
    results= database.exec(statement)
    items = results.all()
    return items

@app.get("/movies/{id}")
async def get_movie_id(id: int, database:SessionDep):
    movie = database.get(MoviesModel,id)
    
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Pelicula no encontrada")
    return movie
