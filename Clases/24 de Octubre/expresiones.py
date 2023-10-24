from collections import namedtuple
from datetime import datetime
from matplotlib import pyplot as plt

Automovil = namedtuple('Automovil', 'nombre fecha, electrico, colores, paises, matriculaciones')
a1 = []
a2 = []
a3 = []

print("---Expresiones---")
a1.fecha < 2023
a2.electrico and 'NEGRO' in a2.colores
a3.matriculaciones[-1] == '5434MLP'
not a1.electrico and not a3.electrico and a2.electrico
len(a2.matriculaciones) >= 2
'ESPAÑA' in a1.paises and not 'ITALIA' in a1.paises
len(a1.paises) > len(a2.paises) and len(a1.paises) < len(a2.paises)
a2.matriculaciones[0][0] == a3.matriculaciones[0][0]
