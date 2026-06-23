import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
movies = pd.read_csv("movies.csv")

encoded = pd.get_dummies(movies["Genre"]).astype(int)

print(encoded)

features = pd.concat(
    [encoded, movies[["Rating"]]],
    axis=1
)

print(features)

similarity_matrix = cosine_similarity(features)
print(similarity_matrix[0])

genre_features=pd.get_dummies(movies["Genre"]).astype(int)
similarity_matrix = cosine_similarity(genre_features)
print(similarity_matrix[0])
