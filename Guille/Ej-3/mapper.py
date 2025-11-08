#!/usr/bin/env python3
# mapper.py para Precio promedio de acciones por anyo
# Procesa datos de Yahoo Finance (CSV)

import sys

for line in sys.stdin:
    line = line.strip()
    
    # Saltar lineas vacías
    if not line:
        continue
    
    fields = line.split(',')

    # CSV format: Date,Open,High,Low,Close,Volume,Adj Close
    # Ejemplo: 2004-08-19,100.01,104.06,95.96,100.335,44659000,100.335
    if len(fields) >= 7:
        try:
            date = fields[0]  # Formato: YYYY-MM-DD
            
            # Saltar el encabezado (si contiene "Date")
            if date.lower() == 'date':
                continue
            
            year = date.split('-')[0]  # Extraer el anyo

            # Usar el precio de cierre ajustado (Adj Close)
            adj_close = float(fields[6])

            # Emitir: anyo TAB precio
            print("{}\t{}".format(year, adj_close))
        except (ValueError, IndexError):
            # Ignorar lineas con formato incorrecto
            continue