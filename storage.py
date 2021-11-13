import csv

allMovies = []

file = open('final.csv')
reader = csv.reader(file)

data = list(reader)
allMovies = data[1:]

likedMovies = []
dislikedMovies = []
notWatchedMovies = []