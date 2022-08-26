
import csv

from numpy import append
with open("finalMovie.csv",encoding="utf-8")as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]
    headers=data[0]
headers.append("posterlink")
#print(headers)

with open("movie_links.csv",encoding="utf-8")as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies_links=data[1:]

with open("movies.csv","a+",newline="",encoding="utf-8")as f:
    writer=csv.writer(f)
    writer.writerow(headers)

for i in all_movies:
    posterfound=any(i[8] in j for j in all_movies_links)
    if posterfound:
        for j in all_movies_links:
            if i[8] == j[0]:
                i.append(j[1])
                if len(i)==28:
                    with open("movies.csv","a+",newline="",encoding="utf-8")as f:
                        writer=csv.writer(f)
                        writer.writerow(i)

