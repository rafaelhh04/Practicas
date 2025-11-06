#!/usr/bin/python
# reducer.py para calcular precio promedio por año
# Calcula el promedio de los precios por año

import sys

current_year = None
total_price = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()

    try:
        year, price = line.split('\t', 1)
        price = float(price)
    except:
        continue

    # Si es el mismo año, acumular
    if current_year == year:
        total_price += price
        count += 1
    else:
        # Nuevo año: emitir el promedio del año anterior
        if current_year:
            average = total_price / count
            print("{}\t{}".format(current_year, average))

        current_year = year
        total_price = price
        count = 1

# Emitir el último año
if current_year:
    average = total_price / count
    print("{}\t{}".format(current_year, average))
