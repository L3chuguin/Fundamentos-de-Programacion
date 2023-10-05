import csv
from collections import namedtuple
Persona = namedtuple ("Persona", "nombre,peso,altura")

def leer_personas1(fichero):
    '''
    Leerá el fichero y devuelve su contenido
    para fichero string y tiene la dirección relativa del fichero
    return del tipo string (str) y contiene los datos del fichero
    '''
    f =open(fichero, encoding='utf-8')
    resultado = f.read()
    f.close
    return resultado

def leer_personas2(fichero):
    '''
    Leerá el fichero y devuelve su contenido
    para ficher string y tiene la dirección relativa del fichero
    return [str] y contiene los datos del fichero
    '''

    resultado = []
    f = open(fichero, encoding='utf-8')
    for linea in f:
        resultado.append(linea)
    f.close()
    return resultado

def leer_personas3(fichero):
    '''
    Leerá el fichero y devuelve su contenido
    para fichero str y tiene la dirección relativa del fichero
    return ([str,str,str]) y contiene los datos del fichero
    '''

    resultado = []
    f = open(fichero, encoding='utf-8') #Sin acabar
    return resultado

def leer_personas(fichero):
    red = []
    with open(fichero, encoding='utf-8') as f:
        next(f)
        for linea in f:
            aux = linea.split(',')
            resultado = []
            resultado.append((aux[0],int(aux[1]),float(aux[2])))
        return resultado
                