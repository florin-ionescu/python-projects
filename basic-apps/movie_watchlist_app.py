import json
from pathlib import Path


#constant variable
WATCHLIST_FILE = Path('watchlist.json')


def load_movie():
    """loads movies from the json file"""
    if not WATCHLIST_FILE.exists():
        return []

    try:
        with WATCHLIST_FILE.open("r", encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_movies(movies):
    """saves movies to the JSON file"""
    with WATCHLIST_FILE.open('w', encoding="utf-8") as file:
        json.dump(movies, file, indent=4)

def show_movies(movies):
    """Display all movies in the watchlist"""
    print("\n--- Movie Watchlist ---")

    if not movies:
        print("Your watchlist is empty.")

    for index, movie in enumerate(movies, start=1):
        status = "Watched" if movie["watched"] else "Not watched"
        print(
            f'{index}. {movie["title"]}'
            f'({movie["year"]}) - {movie["genre"]} - {status}'
            )

def add_movie(movies):
    """Add a new movie"""
    print("\n--- Add Movie ---")

    title = input("Movie title: ").strip()
    genre = input("Genre: ").strip()
    year = input("Release year: ").strip()

    if not title:
        print("Movie title cannot be empty")
        return

    if not year.isdigit():
        print("Release year must be a number.")
        return

    movie = {
        "title": title,
        "genre": genre if genre else "Unknown",
        "year": int(year),
        "watched": False
    }

    movies.append(movie)
    save_movies(movies)

    print(f'"{title}" was added to your watchlist.')

def mark_as_watched(movies):
    """Mark a selected movie as watched"""
    show_movies(movies)

    if not movies:
        return

    choice = input("\nEnter the movie number: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(movies):
        print("Movies number not found.")

    movies[index]["watched"] = True
    save_movies(movies)

    print(f'"{movies[index]["title"]}" was marked as watched.')


def remove_movie(movies):
    """remove the movie selected"""
    show_movies(movies)

    if not movies:
        return

    choice = input("\nEnter the movie number to remove: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(movies):
        print("Movie not found")
        return

    removed_movie = movies.pop(index)
    save_movies(movies)

    print(f'"{removed_movie["title"]} was removed')

def search_movies(movies):
    """Search movies by title."""
    search_term = input("\nEnter a movie title: ").strip().lower()

    if not search_term:
        print("Search text cannot be empty.")
        return

    results = [
        movie
        for movie in movies
        if search_term in movie["title"].lower()
    ]

    if not results:
        print("No matching movies found.")
        return

    print("\n--- Search Results ---")

    for movie in results:
        status = "Watched" if movie["watched"] else "Not watched"
        print(
            f'{movie["title"]} ({movie["year"]}) '
            f'- {movie["genre"]} - {status}'
        )


def main():
    movies = load_movie()

    while True:
        print("\n=== Movie Watchlist App ===")
        print("1. Show watchlist")
        print("2. Add movie")
        print("3. Mark movie as watched")
        print("4. Remove movie")
        print("5. Search movie")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_movies(movies)
        elif choice == "2":
            add_movie(movies)
        elif choice == "3":
            mark_as_watched(movies)
        elif choice == "4":
            remove_movie(movies)
        elif choice == "5":
            search_movies(movies)
        elif choice == "6":
            print("Application closing.")
            break
        else:
            print("Invalid option. Choose a number from 1 to 6.")


if __name__ == '__main__':
    main()