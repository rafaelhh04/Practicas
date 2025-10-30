import sys
import re

# Buscar líneas que contengan "ERROR" o "WARN"
pattern = re.compile(r'(zoroaster)', re.IGNORECASE)

for line in sys.stdin:
    line = line.strip()
    
    if pattern.search(line):
        # Emitir la línea completa
        # La clave es null porque no necesitamos agrupar
        print(f"{line}")

