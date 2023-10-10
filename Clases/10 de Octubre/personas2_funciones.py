import csv
import statistics
from matplotlib import pyplot as plt
from collections import namedtuple
from datetime import datetime
Persona = namedtuple ("Persona", "nombre,apellido,peso,altura,fecha,paro")

def leer_personas(fichero):
    with open(fichero,encoding='utf-8') as f:
        respuesta = []
        lector = csv.reader(f) #Convierte la línea en una secuencia de tipo list
        next(lector)
        for linea in lector:
            linea[4] = datetime.strptime(linea[4],'%d/%m/%y')
            if linea[5] == '5':
                linea[5] = True
            else:
                linea[5] = False

            respuesta.append(Persona(linea[0],linea[1],int(linea[2]),float(linea[3]),linea[4],linea[5])) # Append solo necesita un parámetro, por eso la lista está separada por comas

    return respuesta

def lista_ordenada_de_inc(Personas):
    lista_inc = []
    for p in Personas:
        lista_inc.append(p.peso/(p.altura**2))
    return sorted(lista_inc, reversed = True) # De forma natural sorted te devuelve de menor a mayor, con el reverse lo hacemos de mayor a menor

def lista_nombre_peso_mayores(Personas, altura): # Personas mayores a una altura dada
    lista = []
    for p in Personas, altura:
        if Persona.altura > altura:
            lista.append((p.nombre, p.peso))
    return lista

def niideaestetionosabaescribir(Personas, altura, peso): # Personas mayores a una altura y peso dado
    resultado = True
    for p in Personas:
        if altura > altura:
            if p.peso <= peso:
                resultado = False
    return resultado