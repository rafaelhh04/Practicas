#!/usr/bin/python
# mapper.py para Job 1: Calcular valoracion promedio por pelicula
# Procesa datos de MovieLens (ratings.csv)

import sys
import csv

# Saltar la primera linea (encabezado)
reader = csv.reader(sys.stdin)

# Saltar header si existe
try:
    next(reader)  # Omitir primera línea
except StopIteration:
    pass
for line in reader:

    # CSV format: userId,movieId,rating,timestamp
    # Ejemplo: 1,1,4.0,964982703
    if len(line) >= 3:
        try:
            movie_id = line[1]
            rating = float(line[2])

            # Emitir: movieId TAB rating
            print("{}\t{}".format(movie_id, rating))
        except:
            continue
