import requests

def get_movie(movie):
    try:
        url = "https://www.omdbapi.com/"
        params = {
            "s": movie,
            "apikey": "171fbd6"
        }
    except Exception:
         return None    

    response = requests.get(url, params=params)
    return response.json()

def get_movie_details(imdb_id):
    url = "https://www.omdbapi.com/"
    params = {
        "i": imdb_id,
        "apikey": "171fbd6"
    }

    response = requests.get(url, params=params)
    return response.json()

def main():
    query = input("Search movie: ")

    data = get_movie(query)

    if data["Response"] == "True":

        movies = data["Search"]

        # show list with numbers
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie['Title']} ({movie['Year']})")

        # user selection
        choice = int(input("\nEnter choice number: "))

        # convert choice → index
        selected_movie = movies[choice - 1]

        # extract imdbID
        imdb_id = selected_movie["imdbID"]

        print("\nSelected IMDb ID:", imdb_id)

        # fetch full details
        details = get_movie_details(imdb_id)

        print("\n--- FULL MOVIE DETAILS ---")
        print("Title:", details["Title"])
        print("Year:", details["Year"])
        print("Director:", details["Director"])
        print("Plot:", details["Plot"])

    else:
        print("Error:", data["Error"])


if __name__ == "__main__":
    main()