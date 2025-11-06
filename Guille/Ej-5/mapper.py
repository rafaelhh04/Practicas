#!/usr/bin/python
# mapper.py para calcular masa promedio de meteoritos por tipo
# Procesa datos de NASA Meteorite Landings (CSV)

import sys
import csv

print("DEBUG: Mapper iniciado", file=sys.stderr)

# Saltar la primera linea (encabezado)
reader=csv.reader(sys.stdin, delimiter=';')# Saltar header si existe
try:
    header = next(reader)  # Omitir primera línea
    print("DEBUG: Header encontrado: {}".format(header), file=sys.stderr)
except StopIteration:
    print("DEBUG: No hay header", file=sys.stderr)
    pass



for line in reader:
    

    # CSV format (puede variar, tipicamente):
    # name,id,nametype,recclass,mass (g),fall,year,reclat,reclong,GeoLocation
    # Buscar recclass (tipo) y mass
    # Formato comun: columnas pueden estar en diferentes posiciones

    if len(line) >= 5:
        try:
            # Intentar parsear asumiendo formato est�ndar
            # name, id, nametype, recclass, mass...
            recclass = line[3].strip()  # Tipo de meteorito
            mass_str = line[4].strip()  # Masa en gramos


            # Ignorar si no tiene masa
            if mass_str and mass_str != '' and mass_str.lower() != 'null':
                mass = float(mass_str)

                # Emitir: tipo TAB masa
                print("{}\t{}".format(recclass, mass))
                processed_count += 1
            
        except Exception as e:
            continue
 
