#!/usr/bin/python
# mapper.py para calcular masa promedio de meteoritos por tipo
# Procesa datos de NASA Meteorite Landings (CSV)

import sys

# Saltar la primera linea (encabezado)
first_line = True

for line in sys.stdin:
    if first_line:
        first_line = False
        continue

    line = line.strip()
    fields = line.split(',')

    # CSV format (puede variar, tipicamente):
    # name,id,nametype,recclass,mass (g),fall,year,reclat,reclong,GeoLocation
    # Buscar recclass (tipo) y mass
    # Formato comun: columnas pueden estar en diferentes posiciones

    if len(fields) >= 5:
        try:
            # Intentar parsear asumiendo formato est�ndar
            # name, id, nametype, recclass, mass...
            recclass = fields[3].strip()  # Tipo de meteorito
            mass_str = fields[4].strip()  # Masa en gramos

            # Ignorar si no tiene masa
            if mass_str and mass_str != '' and mass_str.lower() != 'null':
                mass = float(mass_str)

                # Emitir: tipo TAB masa
                print("{}\t{}".format(recclass, mass))
        except:
            continue
