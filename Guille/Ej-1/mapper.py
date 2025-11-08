#!/usr/bin/python
# -*- coding: utf-8 -*-
# mapper.py para Distributed Grep
# Grep distribuido: buscar líneas que contienen una palabra específica (-iw)

import sys
import re

# La palabra a buscar se pasa como argumento
if len(sys.argv) < 2:
    sys.exit("Usage: mapper.py <word>")

search_word = sys.argv[1].lower()

# Procesar cada línea que llega por entrada estándar
for line in sys.stdin:
    # Eliminar salto de línea al final
    line = line.strip()

    # Extraer todas las palabras de la línea (solo letras)
    words = re.findall(r'\b[a-z]+\b', line.lower())

    # Si la palabra buscada está en las palabras de la línea (-iw: word boundary)
    if search_word in words:
        # Emitir la línea completa (como hace grep)
        print(line)