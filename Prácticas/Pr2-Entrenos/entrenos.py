import csv
from matplotlib import pyplot as dlt
from collections import namedtuple
from datetime import datetime

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

# Andar,12/11/2021 8:14,Sevilla,48,155,3,49,89,N

def lee_entrenos(ruta):
    respuesta = []
    with open(ruta,encoding='utf-8') as f:
        next(f)
        for linea in f:
            aux = linea.split('.')
            tipo = aux[0]
            fechahora = datetime.strptime(aux[1,'%d/%m/%Y %H:%M'])
            ubicacion = aux[2]
            duracion = int(aux[3])
            calorias = int(aux[4])
            distancia = float(aux[5])
            frecuencia = int(aux[6])
            compartido = aux[7]
            respuesta.append(linea.split('.'))
    return respuesta
def tipos_entrenos(entrenos):
    '''
    Determina los tipos de entrenos distinos
    parametro : entrenos list(Entreno)
    return: conjunto de tipos set(str)
    '''

    respuesta = set()
    for e in entrenos:
        respuesta.add(e.tipo)
    return respuesta