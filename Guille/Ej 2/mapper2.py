#!/usr/bin/python
# mapper2.py para Job 2: Preparar datos para Top 100
# Lee la salida del Job 1 (recurso TAB count) y la prepara para el reducer

import sys

for line in sys.stdin:
    line = line.strip()

    try:
        resource, count = line.split('\t', 1)
        count = int(count)

        # Emitir con clave fija para que todo vaya al mismo reducer
        # Formato: "top" TAB count TAB resource
        print("top\t{}\t{}".format(count, resource))
    except:
        continue
