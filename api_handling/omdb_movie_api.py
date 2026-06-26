import requests

def get_movie(movie):
    url = "https://www.omdbapi.com/"
    params = {
        "t": movie,
        "apikey": "171fbd6"
    }

    response = requests.get(url, params=params)
    return response.json()


def main():
    movie = input("Enter Movie Title: ")

    data = get_movie(movie)

    if data["Response"] == "True":
        print(f"Title      : {data['Title']}")
        print(f"Released   : {data['Released']}")
        print(f"Director   : {data['Director']}")
    else:
        print(data["Error"])


if __name__ == "__main__":
    main()