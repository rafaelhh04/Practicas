#!/usr/bin/env python3
# mapper2.py para Job 2: Agrupar peliculas por rango de valoracion

import sys

def get_range(rating):
    if 0 <= rating <= 1:
        return "Rango 1: [0, 1]"
    elif 1 < rating <= 2:
        return "Rango 2: (1, 2]"
    elif 2 < rating <= 3:
        return "Rango 3: (2, 3]"
    elif 3 < rating <= 4:
        return "Rango 4: (3, 4]"
    elif 4 < rating <= 5:
        return "Rango 5: (4, 5]"
    else:
        return None

for line in sys.stdin:
    line = line.strip()

    try:
        movie_id, avg_rating = line.split('\t', 1)
        avg_rating = float(avg_rating)

        range_label = get_range(avg_rating)

        if range_label:
            print("{}\t{}".format(range_label, movie_id))
    except:
        continue