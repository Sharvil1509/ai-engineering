import pandas as pd

df_movies = pd.DataFrame({
    "MovieID": [1, 2, 3],
    "Title": ["Titanic", "Inception", "Avatar"]
})

df_ratings = pd.DataFrame({
    "MovieID": [1, 2, 3],
    "Rating": [8.0, 8.8, 7.9]
})

merged = pd.merge(df_movies, df_ratings, on="MovieID")

print(merged)