from src.libraries.imc import Imc


def leer_imc_de_archivo(ruta, nombreArchivo):
    lista_de_imc = []
    with open(ruta + nombreArchivo, "r") as archivo:
        linea = archivo.readline()
        while linea:
            datos = linea.split('-')
            imc_leido_de_linea = Imc(float(datos[1]), float(datos[2]), datos[0])
            imc_leido_de_linea.calcular_imc()
            lista_de_imc.append(imc_leido_de_linea)
            linea = archivo.readline()
    return lista_de_imc

