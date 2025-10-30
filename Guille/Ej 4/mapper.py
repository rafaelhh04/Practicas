#!/usr/bin/python
# mapper.py para Job 1: Calcular valoración promedio por película
# Procesa datos de MovieLens (ratings.csv)

import sys

# Saltar la primera línea (encabezado)
first_line = True

for line in sys.stdin:
    if first_line:
        first_line = False
        continue

    line = line.strip()
    fields = line.split(',')

    # CSV format: userId,movieId,rating,timestamp
    # Ejemplo: 1,1,4.0,964982703
    if len(fields) >= 3:
        try:
            movie_id = fields[1]
            rating = float(fields[2])

            # Emitir: movieId TAB rating
            print("{}\t{}".format(movie_id, rating))
        except:
            continue
