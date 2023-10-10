from personas2_funciones import *
def test_lectura():
    respuesta = leer_personas('.\data\personas2.csv')
    print("El contenido del fichero es: ")
    print(respuesta)