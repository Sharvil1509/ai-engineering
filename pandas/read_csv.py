import pandas as pd

df = pd.read_csv("movies.csv")
print(df)
print(type(df))
print(df.dtypes)

print(df.isna())
print(df[df["Rating"].isna()])
print(df[df["Year"].isna()])
print(df.isna().sum())