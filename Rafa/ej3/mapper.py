#!/usr/bin/env python3
import sys
import csv

# Usar el módulo csv para parsear correctamente
reader = csv.reader(sys.stdin)
# Saltar header si existe
try:
    next(reader)  # Omitir primera línea
except StopIteration:
    pass
for row in reader:
    # Formato esperado: Date,Open,High,Low,Close,Volume,Adj Closeç
    if len(row) >= 5:
        date_str  = row[0]
        close_price = float(row[4])  # Columna "Close"
        if '-' in date_str:
            # Formato ISO: YYYY-MM-DD
            year = date_str.split('-')[0]
        else:
            continue  # Formato no reconocido
        # Agrupar por categoría
        print(f"{year}\t{close_price}\t1")
