import sys
import re

# Validación de argumentos
if len(sys.argv) < 2:
    print("Error: Debes especificar la palabra a buscar", file=sys.stderr)
    print("Uso: mapper1.py <palabra>", file=sys.stderr)
    sys.exit(1)

# Variable a buscar pasada por argumento en minúsculas
search_word = sys.argv[1].lower()

# PROCESAMIENTO
for line in sys.stdin:
    # Preservar línea original (para mantener formato)
    original_line = line.rstrip('\n\r')
    
    # Convertir a minúsculas solo para la comparación
    line_lower = original_line.lower()
    
    # REGEX: \b = word boundary (límite de palabra)
    # "zoroaster" coincide, pero "zoroasters" o "azoroaster" NO
    pattern = r'\b' + re.escape(search_word) + r'\b'

    if re.search(pattern, line_lower):
        # Imprime la palabra y 1 
        print(f"1\t{search_word}")
