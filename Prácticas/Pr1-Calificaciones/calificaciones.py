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


def nota_cuatrimestre(listaExaTeoricos, examenPractico):

    notaTeorico1 = a_cero(listaExaTeoricos[0])
    notaTeorico2 = a_cero(listaExaTeoricos[1])

    examenPractico = a_cero(examenPractico)

    if nota_teoria(notaTeorico1, notaTeorico2) == 0:
        resultado = 0
    else:
        resultado = 0.1 * (notaTeorico1 + notaTeorico2) + 0.8 * examenPractico

    return resultado


def nota_continua(listaExaTeoricos, listaExaPracticos):
    notaCruatrimestre1 = a_cero(nota_cuatrimestre((listaExaTeoricos[0], listaExaTeoricos[1]), listaExaPracticos[0]))
    notaCuatrimestre2 = a_cero(nota_cuatrimestre((listaExaTeoricos[2], listaExaTeoricos[3]), listaExaPracticos[1]))

    resultado = (notaCruatrimestre1 + notaCuatrimestre2) / 2

    if (notaCruatrimestre1 == 0 or notaCuatrimestre2 == 0) and resultado > 4:
        resultado = 4

    return resultado


def definir_guion(valor):
    if valor == "-":
        valor = 0
    return valor