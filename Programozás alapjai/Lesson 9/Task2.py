import csv

def read_movies():
    movies = []
    filename = "movies.csv"
    with open(filename) as file:
        movies_csv = csv.reader(file)
        lines = [tuple(line) for line in movies_csv]
        # for line is movies_csv:
        # lines.append(tuple(line))

        lines = lines[1:]
        for line in lines:
            movies.append((line[0], line[1], line[2], line[3], int(line[3]), int(line[4])))
    return sorted(movies)


movies = read_movies()

print(len(movies))
for movie in movies[5:10]:
    print(f"{movie[0]}, {movie[1]}, {movie[3]}")

for movie in movies:
    if movie[4] > 2010:
        print(f"{movie[0]}, {movie[1]}")