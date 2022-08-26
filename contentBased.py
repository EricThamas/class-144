from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

df=pd.read_csv("movies.csv")
df=df[df["tags"].notna()]


count=CountVectorizer(stop_words="english") 
count_matrix=count.fit_transform(df["tags"])
cosine_score=cosine_similarity(count_matrix) 
# print(cosine_score)  
# print(count_matrix) 

df = df.reset_index() 
indice= pd.Series(df.index, index=df["title"])

def getMovieRecommendation(title): 
    idx= indice[title] 
    sim_score= list(enumerate(cosine_score[idx])) 
    sim_score= sorted(sim_score,key=lambda x:x[1], reverse=True) 
    # print(sim_score) 
    sim_score=sim_score[1:11] 
    movie_indice= [i[0] for i in sim_score] 
    return df["original_title","posterlink","runtime","release_date","vote_average","overview"].iloc[movie_indice].values.tolist()