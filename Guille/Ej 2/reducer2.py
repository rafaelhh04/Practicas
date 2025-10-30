#!/usr/bin/python
# -*- coding: utf-8 -*-
# reducer2.py para Job 2: Encontrar Top 100 recursos
# Mantiene los 100 recursos más accedidos

import sys
import heapq

# Usamos un heap para mantener solo los top 100
top_resources = []

for line in sys.stdin:
    line = line.strip()

    try:
        # Formato de entrada: "top" TAB count TAB resource
        parts = line.split('\t')
        if len(parts) >= 3:
            key = parts[0]
            count = int(parts[1])
            resource = '\t'.join(parts[2:])  # Por si el resource tiene tabs

            # Agregar al heap (min-heap, por eso usamos count directamente)
            heapq.heappush(top_resources, (count, resource))

            # Si tenemos más de 100, remover el menor
            if len(top_resources) > 100:
                heapq.heappop(top_resources)
    except:
        continue

# Ordenar en orden descendente y emitir
top_resources.sort(reverse=True)

for count, resource in top_resources:
    print("{}\t{}".format(resource, count))
