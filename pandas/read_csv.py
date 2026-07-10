import pandas as pd

df = pd.read_csv("movies.csv")
print(df)
print(type(df))
print(df.dtypes)

#find missing values
print(df.isna())
print(df[df["Rating"].isna()])
print(df[df["Year"].isna()])
print(df.isna().sum())

#cleaning missing data
filled_df = df.fillna(0)
print(filled_df)

df["Rating"] = df["Rating"].fillna(0)
print(df)

