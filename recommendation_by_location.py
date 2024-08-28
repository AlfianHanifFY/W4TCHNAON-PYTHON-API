# %%
# libraries: pandas
# input: string of user's country
# file csv: movies, countries

import pandas as pd
pd.set_option('display.max_columns', None)



# hilangkan baris data untuk film berasal dari amerika dan inggris


def recommendation_by_location(df_movies, df_countries, input_country):
    # rekomendasi berdasarkan lokasi user
    other_country_list = []
    for country in input_country:
        other_country_list.append(df_countries[df_countries["country"] != country])
    other_country = pd.concat(other_country_list, ignore_index=True)

    # mengurutkan berdasarkan nilai rating
    other_country_movies = other_country.merge(df_movies[['id', 'rating']], on='id')
    other_country_movies = other_country_movies.drop_duplicates(subset='id')
    other_country_movies = other_country_movies.sort_values(by='rating', ascending=False)

    # output 10 film teratas berdasarkan rating
    result = []
    for _, row in other_country_movies.head(18).iterrows():
        top_other_country_movies = df_movies.loc[df_movies['id'] == row['id']]['id'].values[0]
        result.append(str(top_other_country_movies))
        
    result = [{'id' : str(x)} for x in result] 
        
    return result


