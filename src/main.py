from src.libraries.imc import Imc
from src.libraries.utils import leer_imc_de_archivo

lista = leer_imc_de_archivo('../files/' , 'historial.txt')

for imc in range(0, len(lista)):
    print(lista[imc].mostrar_fecha())
    lista[imc].calcular_imc()
    print(lista[imc].mostrar_imc())
    lista[imc].evaluar_composicion_corporal()
    print(lista[imc].mostrar_composicion_corporal())
    print('--------------------------')
