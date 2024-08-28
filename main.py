from typing import List
from fastapi import FastAPI, Query
from recommendation_by_location import recommendation_by_location
from recommendation_by_movie import recommendation_by_movie
from recommendation_by_actors_genres import recommendation_by_actors_genres
import pandas as pd
import numpy as np

app = FastAPI()
print(np.__version__)
@app.get("/")
def read_root():
    # Read the CSV file into a DataFrame
    df_movies = pd.read_csv('filteredMovies.csv')

    # Convert the DataFrame to a list of dictionaries
    movies_list = df_movies.to_dict(orient="records")

    # Return the list of dictionaries
    return movies_list

@app.get("/data")
def get_recommendation(movieId):
    movieId = int(movieId)
    df_movies = pd.read_csv('filteredMovies.csv')
    return {'movieRecomendation' : recommendation_by_movie(df_movies,movieId)}

@app.get("/dataByCountry")
def get_recommendByCountry(country):
    country = str(country)
    df_movies = pd.read_csv('filteredMovies.csv')
    df_countries = pd.read_csv('filteredCountries.csv')
    # hilangkan baris data untuk film berasal dari amerika dan inggris
    df_countries = df_countries[(df_countries['country'] != 'USA') & (df_countries['country'] != 'UK')]
    return {'movieRecomendation' : recommendation_by_location(df_movies, df_countries, country)}

@app.get("/dataByActorGenre")
def get_recommendByActorGenre(actor: List[str] = Query(...),
    genre: List[str] = Query(...)):
    df_movies = pd.read_csv('filteredMovies.csv')
    df_actors = pd.read_csv('filteredActors.csv')
    df_genres = pd.read_csv('filteredGenres.csv')
    return {"movieRecomendation":recommendation_by_actors_genres(df_movies, df_actors, df_genres, actor, genre)}
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
