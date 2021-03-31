# Programa calculador de Indice de Masa Corporal

### Introducción
 El programa se encarga de calcular el índice de masa corporal(imc) en lenguaje Python.
 
### Documentación

El proyecto lee de la carpeta imc/files el archivo historial.txt y calcula el imc del archivo para mostrarlos en la
terminal.

La clase imc(ubicada en imc/src/libraries) tiene los sigientes métodos:
- calcular_imc -> Calcula el imc, NO LO MUESTRA, lo guarda en el objeto instanciado
- evaluar_composicion_corporal -> Una vez calculado, este método imprime la evaluación según el IMC(Normal, Inferior,
obesidad, etc)
- mostrar_imc -> muestra imc. la función devuelve el imc, no lo imprime la función, sino que LO DEVUELVE
- mostrar_fecha-> muestra fecha. la función devuelve la fecha, no lo imprime la función, sino que LO DEVUELVE
- mostrar_composicion_corporal-> muestra composicion corporal. la función devuelve la composicion corporal, no lo imprime 
la función, sino que LO DEVUELVE

El archivo utils.py(ubicada en imc/src/libraries) cuenta con la siguiente funcion:
leer_imc_de_archivo-> recibe la ruta y el nombre del archivo, lee cada linea, calcula imc y los guarda en una lista

la jerariquía de archivos quedó:
imc
->files
------>historial.txt	(el archivo donde se guardan y leen la fecha, peso y altura)
->src
------>__init__.py
------>main.py		(acá se ejecuta lo que se va a mostrar, por ahora por terminal)
------>libraries
----------->__init__.py
----------->imc.py		(aca está la clase con los metodos del imc)
----------->utils.py		(acá estan las funciones de utilidad del programa, por ahora el que lee los datos del historial)


### Proximas Iteraciones
1) Subir el proyecto a Github(git init en la carpeta, crear el proyecto en la pagina de github y pasarlos al repo remoto.
Certificar que se subió en github propio(karinapiacentini). Crear una rama llamada
agregar_pesaje_historial, en dicha rama se tiene que hacer:
- un menú en el main en donde hayan dos opciones:
	Opcion 1-> Ingresar datos en el historal. Se debe pedir por terminal los datos y se deben guardar como estan
		  (si no se carga así los datos nuevos no se va a leer)
	Opcion 2-> Calcular y mostrar imc. Lo que ya está hecho en main tiene que pasar cuando se selecciona la opción 2
NOTA: Si se tarda más de un día se tiene que subir el progreso a github antes de terminar la jornada(git add, git commit -m
y git push)
Una vez terminado y con el correcto funcionamiento, mergear a main.
PUNTO REALIZADO
  

2) En otra rama llama agregar_conexion_bd hacer:
 Debemos crear una bd llamada programaimc, con una tabla llamada historial_imc con los siguientes datos:
- fecha
- peso
- altura
Ahora el programa debe tomar los datos de la base de datos y no del archivo de historial. Nótese que el imc lo calcula el
programa y NO LO GUARDA. el programa carga los datos(INSERT a la tabla), los obtiene(SELECT a la tabla) y calcula el imc
para luego mostrarlos por pantalla, pero nunca los guarda...Dejar que el programa funcione así.
Una vez terminado y con el correcto funcionamiento, mergear a main.

3) En otra rama llamada creacion_interfaz:
Realizar una interfaz gráfica del programa, existe una librería llamada tkinter que ayuda para dicha feature.
La interfaz se va a realizar en una simple ventana con tres textbox y un boton de "agregar pesaje", un boton 
"ver historial" que muestre en una tabla la fecha, imc y la composición corporal hasta ese momento.
Una vez terminado y con el correcto funcionamiento, mergear a main.
Agregar otro boton para ver el gráfico de avance.

4) Realizar el test integral: En otra rama llamada agregar_test_funcionales:
crear dentro de la carpeta imc otra carpeta llamada tests. Alli crear archivo test_funcional_imc. Se deben realizar
test funcionales a libre creatividad con pytest. Deben contemplar todos los posibles errores.

 
 