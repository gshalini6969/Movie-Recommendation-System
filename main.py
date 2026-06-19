import pandas as pd

movies = pd.read_csv("movies.csv")

movie_name = input("Enter Movie: ").lower()

movie_row=movies[movies["Movie"].str.lower()==movie_name]
if len(movie_row)==0:
    print("Movie not found")
else:
    # Step 1: Find genre
    genre=movies[movies["Movie"].str.lower()==movie_name]["Genre"][0]
    print(genre)
    # Step 2: Find movies with same genre
    same_genre=movies[movies["Genre"]==genre]
    print(same_genre)
    # Step 3: Remove entered movie
    recommendations=same_genre[same_genre["Movie"].str.lower() != movie_name]
    # Step 4: Print recommendations
    print("\nRecommended movies: \n")
    for movie in recommendations["Movie"]:
        print(movie)