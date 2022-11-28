def convert_rgb2gray(lista):
    """Función que convierte una lista de píxeles de espectro de color a otra lista de píxeles en escala de grises
    :parametro rojo: Es un valor que luego se calcula para sacar la luminancia
    :parametro verde: Es un valor que luego se calcula para sacar la luminancia
    :parametro azul: Es un valor que luego se calcula para sacar la luminancia
    :return:"""


    lista = []
    continuar = True
    for y in lista:
        list.append(y + 1)
    return lista


def rgb2gray(rojo, verde, azul):
    """Función que hace la formula de la media para calcular la Luminacia
    :parametro rojo: Es un valor que luego se calcula para sacar la luminancia
    :parametro verde: Es un valor que luego se calcula para sacar la luminancia
    :parametro azul: Es un valor que luego se calcula para sacar la luminancia
    :return: """
    lista = []
    luminancia = 0
    rojo = print(int("Introduce un valor entre 0 a 255 din decimales\n"))
    verde = print(int("Introduce un valor entre 0 a 255 din decimales\n"))
    azul = print(int("Introduce un valor entre 0 a 255 din decimales\n"))

    return print("La Luminancia es: ", int(str(rojo) + str(verde) +str(azul))/3)