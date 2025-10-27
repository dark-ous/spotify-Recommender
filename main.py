import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from numpy import random

df=pd.read_csv("data/SpotifyFeatures.csv")

features=['acousticness', 'danceability', 'energy', 'loudness','speechiness','valence','instrumentalness'] 

X=df[features].values
scalar=StandardScaler()
X=scalar.fit_transform(X)

def cosine_similarity(vector_a,vector_b):
    dot_prod=np.dot(vector_a,vector_b)

    vec_a_mag=np.linalg.norm(vector_a)
    vec_b_mag=np.linalg.norm(vector_b)
    
    if vec_a_mag == 0 or vec_b_mag==0:
        return 0
    return dot_prod/(vec_a_mag*vec_b_mag)

def recommend(query_idx):
    query_vec = df.loc[query_idx, features].values.reshape(1, -1)
    query_vec = scalar.transform(query_vec)
    sims = []
    for i in range(len(X)):
        if query_idx == i:
            sims.append(-1)  
        else: 
            sim = cosine_similarity(query_vec[0], X[i])
            sims.append(sim)
  
    sims = np.array(sims)
    top_indices = sims.argsort()[-10:][::-1]
    return top_indices, sims[top_indices]

query_idx=47342

top_indices,top_sims=recommend(query_idx)

print(f"\033[32mQuery Song:{query_idx}| {df.iloc[query_idx]['track_name']} | {df.iloc[query_idx]['artist_name']} | {df.iloc[query_idx]['genre']} |\033[0m")
print()

for rank, idx in enumerate(top_indices):
    print(f"{rank+1}: {df.iloc[idx]['track_name']}|{df.iloc[idx]['artist_name']}|{df.iloc[idx]['genre']}|Similarity: {top_sims[rank]:.4f}")