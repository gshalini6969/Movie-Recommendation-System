print("Movie Recommendation system")
movies = {"Avatar" : ["Titanic","The Abyss"],"Titanic" : ["Avatar","The Notebook"],"Inception" : ["Interstellar","Tenet"]}
inp=input("Enter movie name: ")
if inp in movies:
    print("Recommended movies: ")
    for movie in movies[inp]:
        print(movie)
else:
    print("Movie not found")
print("Hello you!")
