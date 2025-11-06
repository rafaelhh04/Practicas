#!/usr/bin/python
# reducer2.py para Job 2: Agrupar IDs de películas por rango
# Agrupa todas las películas en cada rango

import sys

current_range = None
movie_ids = []

for line in sys.stdin:
    line = line.strip()

    try:
        range_label, movie_id = line.split('\t', 1)
    except:
        continue

    # Si es el mismo rango, agregar el movie_id
    if current_range == range_label:
        movie_ids.append(movie_id)
    else:
        # Nuevo rango: emitir el rango anterior
        if current_range:
            print("{}\t{}".format(current_range, ','.join(movie_ids)))

        current_range = range_label
        movie_ids = [movie_id]

# Emitir el último rango
if current_range:
    print("{}\t{}".format(current_range, ','.join(movie_ids)))
