import csv

file = open("movies.csv", encoding='utf-8')
reader = csv.reader(file)
data = list(reader)
allMovies = data[1:]
headers = data[0]

headers.append("poster_link")

file = open("final.csv", "a+", encoding='utf-8')
csvwriter = csv.writer(file)
csvwriter.writerow(headers)

file = open("movie_links.csv", encoding='utf-8')
reader = csv.reader(file)
data = list(reader)

all_movie_links = data[1:]

for movieitem in allMovies:
    posterfound = any(movieitem[8] in movielinkitems for movielinkitems in all_movie_links)
    if posterfound:
        for movielinkitem in all_movie_links:
            if movieitem[8] == movielinkitem[0]:
                movieitem.append(movielinkitem[1])
                if len(movieitem) == 28:
                    file = open("final.csv", "a+", encoding='utf-8')
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(movieitem)