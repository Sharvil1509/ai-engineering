import pandas as pd

# Load data
df = pd.read_csv("data/movies.csv")

print("========== DATA ==========")
print(df)

print("\n========== INFO ==========")
df.info()


# 1. Average rating
print("\n========== AVERAGE RATING ==========")
average_rating = df["Rating"].mean()
print(f"Average Rating: {average_rating:.2f}")


# 2. Highest rated movie
print("\n========== TOP RATED MOVIE ==========")
top_movie = df.sort_values("Rating", ascending=False).head(1)
print(top_movie)


# 3. Lowest rated movie
print("\n========== LOWEST RATED MOVIE ==========")
lowest_movie = df.sort_values("Rating").head(1)
print(lowest_movie)


# 4. Count movies by genre
print("\n========== MOVIES BY GENRE ==========")
genre_count = df["Genre"].value_counts()
print(genre_count)


# 5. Average rating by genre
print("\n========== AVERAGE RATING BY GENRE ==========")
genre_rating = df.groupby("Genre")["Rating"].agg(
    ["mean", "max", "min", "count"]
)

print(genre_rating)


# 6. Christopher Nolan movies
print("\n========== NOLAN MOVIES ==========")
nolan_movies = df[df["Director"] == "Christopher Nolan"]
print(nolan_movies)


# 7. Movies after 2010
print("\n========== MOVIES AFTER 2010 ==========")
recent_movies = df[df["Year"] > 2010]
print(recent_movies)


# 8. Create rating category
print("\n========== RATING CATEGORY ==========")

def rating_category(rating):
    if rating >= 9:
        return "Masterpiece"
    elif rating >= 8:
        return "Great"
    else:
        return "Good"


df["Category"] = df["Rating"].apply(rating_category)

print(df)


# 9. Save analyzed data
print("\n========== SAVING FILE ==========")

df.to_csv("data/analyzed_movies.csv", index=False)

print("Saved successfully!")