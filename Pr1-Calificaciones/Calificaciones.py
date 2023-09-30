def nota_teoria(nota1, nota2):
    nota1 = a_cero(nota1)
    nota2 = a_cero(nota2)

    media = (nota1+nota2) / 2

    media = a_cero(media)

    return media

def a_cero(valor):
    resultado = valor
    if resultado == None or resultado < 4:
        resultado = 0
    return resultado