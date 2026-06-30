import pandas as pd

movies = [
    {"Title": "Titanic", "Year": 1997, "Rating": 8.0},
    {"Title": "Inception", "Year": 2010, "Rating": 8.8},
    {"Title": "Interstellar", "Year": 2014, "Rating": 8.7}
]

df = pd.DataFrame(movies)
print(df)

ratings = df[["Title", "Year"]]
print(type(ratings))

print(df["Rating"])

print(type(df["Rating"]))

print(df[["Rating"]])

print(type(df[["Rating"]]))

print(df.iloc[1])

print(type(df.iloc[1]))

print(df.iloc[[1]])

print(type(df.iloc[[1]]))

print(type(df.iloc[2]))
print(type(df.iloc[2:3]))

df = df.set_index("Title")
print(df)