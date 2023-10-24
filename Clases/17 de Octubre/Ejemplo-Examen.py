# Ejercicio 1
 # a) Añadir el valor 10 a conjunto
conjunto.add(8)

 # b) Sustituir el primer elemento de la lista por el valor 20
len[0] = 20

 #c) Sustituir el primer elemento de la tupla por el valor 20 (NO SE PUEDE)

  #d) Eliminar la clave 10 del diccionario
del(diccionario[10])

# Ejercicio 2
 # a)
len(p1.libros_leídos) > 10 and p1.nombre == A

#Ejercicio 4
 # a)
Automovil = namedTuple('Automovil', 'matrícula, nombre, fecha, kilometraje, precio')

 # b)
def lee_automoviles(CSV):
    res =[]
    with open(fichero, encoding=utf-8) as f:
        lector = csv.reader(f)
        for m,n,f.k,p in lector: # f es fecha
            f = datetime.strptime(f,'%d/%m/%Y').date
            k = int(k)
            p = float(p)
        res.append(Automovil, n, m, f, k, p)
        return res

 # c)
def media_kilometros(Automovil, año)
    res = None
    cont, suma = 0;0
    for a in automovil:
        if a.fecha.year == año:
            cont = 1
            suma+ = a.kilometraje
    if cont! = 0:
        res = suma/cont
    return res

lista[3,8,9,11]
enumerate(lista) #[(0,3),(1,8)...] Para saber la posición del número