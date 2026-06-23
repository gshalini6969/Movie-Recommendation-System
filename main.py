import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
movies = pd.read_csv("movies.csv")

# Basic movie-recommendation system (recommendation by genre)
# movie_name = input("Enter Movie: ").lower()

# movie_row=movies[movies["Movie"].str.lower()==movie_name]
# if len(movie_row)==0:
#     print("Movie not found")
# else:
#     # Step 1: Find genre
#     genre=movie_row["Genre"].iloc[0]
#     print(genre)
#     # Step 2: Find movies with same genre
#     same_genre=movies[movies["Genre"]==genre]
#     print(same_genre)
#     # Step 3: Remove entered movie
#     recommendations=same_genre[same_genre["Movie"].str.lower() != movie_name]
#     # Step 4: Print recommendations
#     recommendations = recommendations.sort_values(
#         by="Rating",
#         ascending=False
#     )

#     print("\nRecommended movies: \n")
#     for movie in recommendations["Movie"]:
#         print(movie)
  
# Dataset -> Feature Engineering -> Encoding -> Feature Scaling -> Cosine Similarity -> Ranking -> Top-N Recommendations

encoded = pd.get_dummies(movies["Genre"]).astype(int)
features= pd.concat([encoded , movies[["Rating","Year"]]],axis=1)

scaler=StandardScaler()
scaled_features=scaler.fit_transform(features)

similarity_matrix = cosine_similarity(scaled_features)

movie_name=input("Enter movie: ").lower()
movie_index = movies[
    movies["Movie"].str.lower() == movie_name
].index[0]

scores = list(enumerate(similarity_matrix[movie_index]))
scores=sorted(scores,reverse=True,key=lambda item: item[1])
print("\nTop 3 Recommendations:\n")
for movie_index, score in scores[1:4]:
    print(movies.iloc[movie_index]["Movie"])