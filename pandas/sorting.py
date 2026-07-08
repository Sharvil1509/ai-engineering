import pandas as pd

movies = [
    {"Title": "Titanic", "Year": 1997, "Rating": 8.0},
    {"Title": "Inception", "Year": 2010, "Rating": 8.8},
    {"Title": "Interstellar", "Year": 2014, "Rating": 8.7},
    {"Title": "Avatar", "Year": 2009, "Rating": 7.9}
]

df = pd.DataFrame(movies)

sorted_df = df.sort_values("Year")

print("Original:")
print(df)

print("\nSorted:")
print(sorted_df)

sorted_df1 = df.sort_values("Rating", ascending=False)

print(sorted_df1)