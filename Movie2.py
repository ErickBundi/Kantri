"""
Emmanuela Mbe
CIS 261
Movie Guide Part 2
"""

def display_heading_and_menu():

    print("\nThe Movie List program")
    print("\nCOMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()


def load_movies_from_file(filename):

    movies = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                movie = line.strip()
                if movie:  
                    movies.append(movie)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    
    return movies


def display_movies(movies):

    if not movies:
        print("No movies in the list.")
    else:
        for i, movie in enumerate(movies, 1):
            print(f"{i}. {movie}")


def add_movie(movies):

    movie_title = input("Movie: ")
    if movie_title.strip():
        movies.append(movie_title.strip())
        print(f"{movie_title} was added.")
    else:
        print("Movie title cannot be empty.")


def save_movies_to_file(movies, filename):

    try:
        with open(filename, 'w') as file:
            for movie in movies:
                file.write(movie + '\n')
    except IOError as e:
        print(f"Error writing to file: {e}")


def delete_movie(movies):

    if not movies:
        print("No movies to delete.")
        return
    
    try:
        number = int(input("Number: "))
        if 1 <= number <= len(movies):
            deleted_movie = movies.pop(number - 1)
            print(f"{deleted_movie} was deleted.")
        else:
            print("Invalid movie number.")
    except ValueError:
        print("Invalid movie number.")


def main():

    filename = 'movies.txt'

    movies = load_movies_from_file(filename)   
    while True:
        display_heading_and_menu()
        command = input("Command: ").strip().lower()
        
        if command == "list":
            display_movies(movies)
        
        elif command == "add":
            add_movie(movies)
            save_movies_to_file(movies, filename)
            display_movies(movies)
        
        elif command == "del":
            delete_movie(movies)
            save_movies_to_file(movies, filename)
            display_movies(movies)
        
        elif command == "exit":
            print("Bye!")
            break
        
        else:
            print("Not a valid command. Please try again.")


if __name__ == "__main__":
    main()