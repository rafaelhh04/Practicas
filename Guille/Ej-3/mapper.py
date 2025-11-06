#!/usr/bin/python
# mapper.py para Precio promedio de acciones por año
# Procesa datos de Yahoo Finance (CSV)

import sys

# Saltar la primera línea (encabezado)
first_line = True

for line in sys.stdin:
    if first_line:
        first_line = False
        continue

    line = line.strip()
    fields = line.split(',')

    # CSV format: Date,Open,High,Low,Close,Volume,Adj Close
    # Ejemplo: 2004-08-19,100.01,104.06,95.96,100.335,44659000,100.335
    if len(fields) >= 7:
        try:
            date = fields[0]  # Formato: YYYY-MM-DD
            year = date.split('-')[0]  # Extraer el año

            # Usar el precio de cierre ajustado (Adj Close)
            adj_close = float(fields[6])

            # Emitir: año TAB precio
            print("{}\t{}".format(year, adj_close))
        except:
            continue
