#!/usr/bin/env python3
# reducer.py para Job 1: Calcular promedio de valoracion por pelicula

import sys

current_movie = None
total_rating = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()

    try:
        movie_id, rating = line.split('\t', 1)
        rating = float(rating)
    except:
        continue

    if current_movie == movie_id:
        total_rating += rating
        count += 1
    else:
        if current_movie:
            average = total_rating / count
            print("{}\t{:.2f}".format(current_movie, average))

        current_movie = movie_id
        total_rating = rating
        count = 1

if current_movie:
    average = total_rating / count
    print("{}\t{:.2f}".format(current_movie, average))