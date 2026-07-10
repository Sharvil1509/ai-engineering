import pandas as pd

movies = [
    {"Title": "Titanic", "Genre": "Drama", "Rating": 8.0},
    {"Title": "The Godfather", "Genre": "Drama", "Rating": None},
    {"Title": "Inception", "Genre": "Sci-Fi", "Rating": 8.8},
    {"Title": "Interstellar", "Genre": "Sci-Fi", "Rating": 8.7},
    {"Title": "Avatar", "Genre": "Sci-Fi", "Rating": 7.9},
]

df = pd.DataFrame(movies)

print(df.groupby("Genre").mean(numeric_only=True))
print(df.groupby("Genre").count())# count non missing values
print(df.groupby("Genre").size())# count rows

print(df.groupby("Genre")["Rating"].agg(["mean", "max", "min", "count"]))

print(df["Genre"].value_counts())
print(df.drop(columns=["Genre"]))

#df.to_csv("movies.csv")  ---> DataFrame ── to_csv() ──► CSV