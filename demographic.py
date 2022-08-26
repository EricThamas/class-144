import pandas as pd
import numpy as np

df=pd.read_csv("movies.csv")

c=df["vote_average"].mean()

m=df["vote_count"].quantile(0.9)

qmovies=df.copy().loc[df["vote_count"]>=m]

def weightRating(x): 
    v=x["vote_count"] 
    r=x["vote_average"] 
    return (v/(v+m)*r)+ (m/(v+m)*c) 
qmovies["score"]= qmovies.apply(weightRating,axis=1) 
qmovies=qmovies.sort_values("score",ascending=False)
output=qmovies[["original_title","posterlink","release_date","runtime","vote_average","overview"]].head(20).values.tolist()
