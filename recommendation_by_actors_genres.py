# %%
# libraries: pandas
# input: string actor n genre
# file csv: movies, actors, genres

import pandas as pd
pd.set_option('display.max_columns', None)



def recommendation_by_actors_genres(df_movies, df_actors, df_genres, input_actors, input_genres):
    # rekomendasi berdasarkan aktor favorit
    start_actors_list = []
    for name in input_actors:
        start_actors_list.append(df_actors[df_actors["name"] == name])
    start_actors = pd.concat(start_actors_list, ignore_index=True)

    # rekomendasi berdasarkan genre favorit
    start_genres_list = []
    for genre in input_genres:
        start_genres_list.append(df_genres[df_genres["genre"] == genre])
    start_genres = pd.concat(start_genres_list, ignore_index=True)

    # menggabungkan kedua dataset, diurutkan berdasarkan nilai rating
    start_movies = pd.merge(start_actors, start_genres, on="id")
    start_movies = start_movies.drop_duplicates(subset='id')
    start_movies = start_movies.merge(df_movies[['id', 'rating']], on='id')
    start_movies = start_movies.sort_values(by='rating', ascending=False)
    result = []
    # output 10 film teratas berdasarkan rating
    for _, row in start_movies.head(19).iterrows():
        result.append(df_movies.loc[df_movies['id'] == row['id']]['id'].values[0])
    

    result = [{'id' : str(x)} for x in result]  
    return result
