#!/usr/bin/python
# -*- coding: utf-8 -*-
# mapper.py para Job 1: Contar accesos a recursos
# Parsea Common Log Format y extrae el recurso (sin query string)

import sys
import re

# Regex para parsear Common Log Format (CLF)
# Ejemplo: 127.0.0.1 - - [01/Aug/1995:00:00:01 -0400] "GET /images/logo.gif HTTP/1.0" 200 1234
clf_pattern = re.compile(r'^(\S+) \S+ \S+ \[(.*?)\] "(\S+) (\S+) (\S+)" (\d+) (\S+)')

for line in sys.stdin:
    line = line.strip()
    match = clf_pattern.match(line)

    if match:
        # Extraer el recurso (URL solicitada)
        resource = match.group(4)

        # Remover el query string (lo que viene despues de ?)
        if '?' in resource:
            resource = resource.split('?')[0]

        # Emitir: recurso TAB 1
        print("{}\t1".format(resource))
