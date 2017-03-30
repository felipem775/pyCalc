import sys
import re
if len(sys.argv) != 3:
    print("El script debe recibir dos parámetros a sumar")

elif  re.match("^[+-]?\d(>?\.\d+)?$", sys.argv[1]) is None:
    print("El primer parámetro no es un número")

elif  re.match("^[+-]?\d(>?\.\d+)?$", sys.argv[2]) is None:
    print("El segundo parámetro no es un número")

else:
    print(int(sys.argv[1]) + int(sys.argv[2]))
