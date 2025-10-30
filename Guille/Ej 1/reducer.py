#!/usr/bin/python
# -*- coding: utf-8 -*-
# reducer.py para Distributed Grep
# Simplemente pasa todas las lineas que recibe del mapper

import sys

# El mapper ya filtro las lineas, el reducer solo las imprime
for line in sys.stdin:
    # Eliminar salto de linea y reimprimir
    print(line.strip())
