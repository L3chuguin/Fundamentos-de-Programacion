from collections import namedtuple
import csv

Registro = namedtuple("Registro","nombre, precio, iva, unidades, descuento")
def leer_fichero(fichero):
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        res = []
        for i in lector:
            precio = float(precio)
            iva = int(iva)
            unidades = int(unidades)
            descuento = int(descuento)
        res.append(Registro(i[0], precio, iva, unidades, descuento))

def calcular_valor(precio,iva,unidades=1,descuento=5):
    neto = precio*(1-descuento/100)*unidades
    return neto(1+iva/100)

def total_valor(datos):
    suma = 0
    for a in datos:
        suma += calcular_valor(a.precio,a.iva,a.unidades,a.descuento)
    return suma

def genera_factura(datos,nombre_fichero):
    with open(nombre_fichero,mode = 'w' ,encoding='utf-8') as f:
        total = 0.0
        f.write('\n'+nombre precio iva unidades descuento parcial')
                for nombre, precio, iva, unidades, descuento in lista:
                    parcial = total_valor(precio,iva,unidades,descuento)
                    total += parcial
                    f.write('\n'+nombre + '\t' + str(precio) + '\t'str(iva) +'\t'str(descuento)) #\t es para ir un renglón mas abajo
                f.write('\n\n'+"Total factura ******************** " +str(total_valor))
                