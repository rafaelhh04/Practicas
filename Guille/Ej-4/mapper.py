#!/usr/bin/env python3
# mapper.py para Job 1: Calcular valoracion promedio por pelicula

import sys
import csv

reader = csv.reader(sys.stdin)

# Saltar header si existe
try:
    next(reader)
except StopIteration:
    pass

for line in reader:
    # CSV format: userId,movieId,rating,timestamp
    if len(line) >= 3:
        try:
            movie_id = line[1]
            rating = float(line[2])
            print("{}\t{}".format(movie_id, rating))
        except:
            continue