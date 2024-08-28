# %%
# libraries: pandas, nltk, sklearn  
# input: id
# file csv: movies
import pandas as pd
pd.set_option('display.max_columns', None)

df_movies = pd.read_csv('filteredMovies.csv')
df_actors = pd.read_csv('filteredActors.csv')
df_genres = pd.read_csv('filteredGenres.csv')


def recommendation_by_movie(df_movies, movie_id):
    # use stem to simplify words in the 'description' feature
    import nltk
    from nltk.stem.porter import PorterStemmer
    ps = PorterStemmer()

    def stem(text):
        y = []
        for i in text.split():
            y.append(ps.stem(i))
        return " ".join(y)
    
    df_movies["description"] = df_movies["description"].apply(stem)
    
    # use vectorizer to set array needed to do cosine similarity
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(stop_words = "english", max_features = 5000)
    vectors = cv.fit_transform(df_movies["description"]).toarray()

    # do cosine similarity on 'description' feature
    from sklearn.metrics.pairwise import cosine_similarity
    similarity = cosine_similarity(vectors)

    # do recommendation based on cosine similarity for inputted movie_id
    movies_index = df_movies[df_movies['id'] == movie_id].index[0]
    distance = similarity[movies_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key= lambda x : x[1])[1:19]
    result = []
    for i in movies_list:
        similiar_movie = df_movies.iloc[i[0]]['id']
        result.append(similiar_movie)
    result = [{'id' : str(x)} for x in result]
    return result

        


