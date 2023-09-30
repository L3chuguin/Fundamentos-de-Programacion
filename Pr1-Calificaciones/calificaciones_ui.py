from calificaciones import *
def solicita_notas():
    nombre = input("Introduzca su nombre: ")
    notaTeorico1 = float(definir_guion(input("Introduzca la nota del examen teórico 1: ")))
    notaTeorico2 = float(definir_guion(input("Introduzca la nota del examen teórico 2: ")))
    notaTeorico3 = float(definir_guion(input("Introduzca la nota del examen teórico 3: ")))
    notaTeorico4 = float(definir_guion(input("Introduzca la nota del examen teórico 4: ")))
    notaPractico1 = float(definir_guion(input("Introduzca la nota del examen práctico 1: ")))
    notaPractico2 = float(definir_guion(input("Introduzca la nota del examen práctico 2: ")))
    
    coleccionNotas = (nombre, notaTeorico1, notaTeorico2, notaTeorico3, notaTeorico4, notaPractico1, notaPractico2)

    return coleccionNotas

def mostrar_notas(coleccionNotas):
    print(f"Hola, {coleccionNotas[0]}")
    print("Tus notas en el primer cuatrimestre son:")
    print(f"Teoría: {nota_teoria(coleccionNotas[1], coleccionNotas[2])}, Práctica: {coleccionNotas[5]}, Cuatrimestre: {nota_cuatrimestre((coleccionNotas[1], coleccionNotas[2]), coleccionNotas[5])}")
    print("Tus notas tel segundo cuatrimestre son:")
    print(f"Teoría: {nota_teoria(coleccionNotas[3], coleccionNotas[4])}, Práctica: {coleccionNotas[6]}, Cuatrimestre: {nota_cuatrimestre((coleccionNotas[3], coleccionNotas[4]), coleccionNotas[6])}")
    print(f"Tu nota final de la asignatura es: {nota_continua((coleccionNotas[1], coleccionNotas[2], coleccionNotas[3], coleccionNotas[4]), (coleccionNotas[5], coleccionNotas[6]))}")