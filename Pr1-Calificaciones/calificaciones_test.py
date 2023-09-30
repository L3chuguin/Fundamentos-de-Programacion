from calificaciones import *
from calificaciones_ui import *

print ("APARTADO A")
print(f"9.1, 7.2 ==> {nota_teoria(9.1 , 7.2)} ")
print(f"4.0, 6.0 ==> {nota_teoria(4.0 , 6.0)} ")
print(f"4.0, 3.0 ==> {nota_teoria(4.0 , 3.0)} ")
print(f"None, 3.0 ==> {nota_teoria(None , 3.0)} ")
print(f"9.0, None ==> {nota_teoria(9.0 , None)} ")

print ("APARTADO B")

print(f"9.1, 7.2, 8.1 ==> {nota_cuatrimestre((9.1, 7.2), 8.1)}")
print(f"4.0, 6.0, 5.0 ==> {nota_cuatrimestre((4.0, 6.0), 5.0)}")
print(f"4.0, 3.0, None ==> {nota_cuatrimestre((4.0, 3.0), None)}")
print(f"None, 3.0, None ==> {nota_cuatrimestre((None, 3.0), None)}")
print(f"9.0, None, 4.5 ==> {nota_cuatrimestre((9.0, None), 4.5)}")

print ("APARTADO C")

print(f"Notas teoría: 9.6, 9.9, 10.0, 9.8 Notas práctico: 9.7, 9.5 ==> {nota_continua((9.6, 9.9, 10.0, 9.8), (9.7, 9.5))}")
print(f"Notas teoría: 4.4, 4.9, 5.1, 4.7 Notas práctico: 4.6, 4.8 ==> {nota_continua((4.4, 4.9, 5.1, 4.7), (4.6, 4.8))}")
print(f"Notas teoría: 4.9, 6.0, 4.0, 3.0 Notas práctico: 5.0, None ==> {nota_continua((4.9, 6.0, 4.0, 3.0), (5.0, None))}")
print(f"Notas teoría: 9.0, None, 4.0, 3.0 Notas práctico: 4.5, None ==> {nota_continua((9.0, None, 4.0, 3.0), (4.5, None))}")

print("APARTADO D")

mostrar_notas(solicita_notas())