import pandas as pd

# Create DataFrame
movies = [
    {"Title": "Titanic", "Year": 1997, "Rating": 8.0},
    {"Title": "Inception", "Year": 2010, "Rating": 8.8},
    {"Title": "Interstellar", "Year": 2014, "Rating": 8.7},
    {"Title": "Avatar", "Year": 2009, "Rating": 7.9}
]

df = pd.DataFrame(movies)

print("Original DataFrame:")
print(df)

# ------------------------------------
# Boolean Mask
# ------------------------------------

print("\nMovies with Rating > 8.5")

mask = df["Rating"] > 8.5
print(mask)

print("\nFiltered DataFrame:")
print(df[mask])

# ------------------------------------
# AND Filtering
# ------------------------------------

print("\nMovies after 2000 AND Rating > 8.7")

print(
    df[
        (df["Year"] > 2000) &
        (df["Rating"] > 8.7)
    ]
)

# ------------------------------------
# OR Filtering
# ------------------------------------

print("\nMovies after 2000 OR Rating > 8.7")

print(
    df[
        (df["Year"] > 2000) |
        (df["Rating"] > 8.7)
    ]
)