#!/usr/bin/python
# reducer.py para Job 1: Calcular promedio de valoración por película
# Calcula el rating promedio de cada película

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

    # Si es la misma película, acumular
    if current_movie == movie_id:
        total_rating += rating
        count += 1
    else:
        # Nueva película: emitir el promedio de la película anterior
        if current_movie:
            average = total_rating / count
            print("{}\t{}".format(current_movie, average))

        current_movie = movie_id
        total_rating = rating
        count = 1

# Emitir la última película
if current_movie:
    average = total_rating / count
    print("{}\t{}".format(current_movie, average))
