#!/usr/bin/env python3
# reducer2.py para Job 2: Agrupar IDs de peliculas por rango

import sys

current_range = None
movie_ids = []

for line in sys.stdin:
    line = line.strip()

    try:
        range_label, movie_id = line.split('\t', 1)
    except:
        continue

    if current_range == range_label:
        movie_ids.append(movie_id)
    else:
        if current_range:
            print("{}\t{}".format(current_range, ','.join(movie_ids)))

        current_range = range_label
        movie_ids = [movie_id]

if current_range:
    print("{}\t{}".format(current_range, ','.join(movie_ids)))