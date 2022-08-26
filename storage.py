import csv
all_movie=[]
with open("movies.csv",encoding="utf-8")as f:
    reader=csv.reader(f)
    data= list(reader)
    all_movie=data[1:]
    # print(all_movie)

liked_movies=[]
not_liked=[]

did_not_match=[]