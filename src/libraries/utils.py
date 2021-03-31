from src.libraries.imc import Imc
from src.libraries import constantes


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


def app():
    mostrar_menu()

    # Preguntar al usuario la accion que desea utilizar
    preguntar = True
    while preguntar:
        opcion = input("seleccione una opcion \r\n")

        # Ejecutar las diferentes opciones
        if opcion == '1':
            ingresar_datos_a_historial()
            preguntar = False
        elif opcion == '2':
            calcular_mostrar_historial_imc()
            preguntar = False
        elif opcion == '3':
            preguntar = False
            return 0
        else:
            print("Opcion no valida, intente de nuevo")


def ingresar_datos_a_historial():
    print("escribe los datos para agregar al historial")
    fecha_pesaje = input("Fecha en formato DD/MM/AAAA:\r\n")
    peso = input("Agrega el peso: \r\n")
    altura = input("Agrea altura formato M.CC: \r\n")

    imc = Imc(fecha_pesaje, peso, altura)

    with open(constantes.RUTA + constantes.NOMBRE_ARCHIVO, "a") as archivo:

        archivo.write(fecha_pesaje+ "-" + peso + "-" + altura +"\n")

        print("\nDatos ingresados correctamente \r\n ")

    app()


def calcular_mostrar_historial_imc():
    lista = leer_imc_de_archivo(constantes.RUTA, constantes.NOMBRE_ARCHIVO)

    for imc in range(0, len(lista)):
        print(lista[imc].mostrar_fecha())
        lista[imc].calcular_imc()
        print(lista[imc].mostrar_imc())
        lista[imc].evaluar_composicion_corporal()
        print(lista[imc].mostrar_composicion_corporal())
        print('--------------------------')


def mostrar_menu():
    print("seleccione del menu lo que desea hacer:")
    print("1) Ingresar datos a historial.")
    print("2) Calcular y mostrar historial de imc.")
    print("3) Salir.")

