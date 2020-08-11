#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Torres Molina Emmanuel O."
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('\nComenzamos a ponernos serios!.\n\n')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuente cuantos números ingresados hay, y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''

    inicio = int(input('Ingrese el 1er Número Entero de la Secuencia: '))
    fin = int(input('\nIngrese el 2do Número Entero de la Secuencia: ')) 

    # Inicialización de Variables:
    cantidad_numeros = 0
    sumatoria = 0

    secuencia = list(range(inicio, fin + 1))

    print('\n\nEl Rango Ingresado es: [{}, {}]'.format(inicio, fin))
    print('\nLa Secuencia Armada es: {}'.format(secuencia))

    # bucle.....
    for i in range(len(secuencia)):
        cantidad_numeros = i + 1
        sumatoria += secuencia[i]

    # Al terminar el bucle calcular el promedio como:
    # promedio = sumatoria / cantidad_numeros
    promedio = sumatoria / cantidad_numeros

    # Imprimir resultado en pantalla
    print('\n\nLa Cantidad de Números que hay en la Secuencia es: {}'.format(cantidad_numeros))
    print('\nLa Sumatoria de los Números de la Secuencia es: {}'.format(sumatoria))
    print('\nEl Promedio de los Números que están Dentro de la Secuencia es: {}\n\n'.format(promedio))



def ej2():
    print("Mi Calculadora (^_^) :")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''
    palabra = None

    while ((palabra == None) or (palabra != 'FIN')):

        numero_1 = float(input('\n\nIngrese un Número Real: '))
        numero_2 = float (input('\nIngrese Otro Número Real: '))

        print('\n\nAhora Ingrese el Símbolo de la Operación que Desee Calcular o la Palabra "FIN" para Finalizar el Programa.\n')
        print('Suma (+)')
        print('Resta (-)')
        print('Multiplicación (*)')
        print('División (/)')
        print('Exponente/Potencia (**)\n')

        palabra = str(input('Ingrese el Símbolo de la Operación o la Palabra "FIN": '))

        if palabra == '+':
            result = numero_1 + numero_2
            print('\n\nEl Símbolo Ingresado es:"{}" y el Resultado de la Operación es: {}.'.format(palabra, result))

        elif palabra == '-':
            result = numero_1 - numero_2
            print('\n\nEl Símbolo Ingresado es:"{}" y el Resultado de la Operación es: {}.\n\n'.format(palabra, result))

        elif palabra == '*':
            result = numero_1 * numero_2
            print('\n\nEl Símbolo Ingresado es: "{}" y el Resultado de la Operación es: {}.\n\n'.format(palabra, result))

        elif palabra == '/':
            result = numero_1 / numero_2
            print('\n\nEl Símbolo Ingresado es: "{}" y el Resultado de la Operación es: {}.\n\n'.format(palabra, result))

        elif palabra == '**':
            result = numero_1 ** numero_2
            print('\n\nEl Símbolo Ingresado es: "{}" y el Resultado de la Operación es: {}.\n\n'.format(palabra, result))

        else:

            if palabra == 'FIN':
                print('\n\nPrograma Finalizado.\n\n')

            else:
                print('\n\nEl Símbolo Ingresado: "{}" es un Símbolo Matemático Incorrecto.\n\n'.format(palabra))



def ej3():
    print("Mi organizador académico (#_#): \n\n")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento:

    Las notas del estudiante se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe calcular el promedio de todas las notas y luego transformar
    la calificación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''

    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
    sumatoria = 0           # Ya le hemos inicializado en 0

    cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
    cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

    # Realice aquí el bucle para recorrer todas las notas
    # y cacular la sumatoria

    for i in range(len(notas)):
        
        if notas[i] >= 0:
            sumatoria += notas[i]

        else:
            cantidad_ausentes += 1


    cantidad_notas = len(notas) - cantidad_ausentes 

    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas
    promedio = sumatoria / cantidad_notas

    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado

        # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es menor a  60      --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados

    if promedio >= 90:
        print ('\nEl Alumno Obtuvo la Siguiente Calificación: A\n')

    elif promedio >= 80:
        print('\nEl Alumno Obtuvo la Siguiente Calificación: B\n')

    elif promedio >= 70:
        print('\nEl Alumno Obtuvo la Siguiente Calificación: C\n')

    elif promedio >= 60:
        print('\nEl Alumno Obtuvo la Siguiente Calificación: D\n')

    else:
        print('\nEl Alumno Obtuvo la Siguiente Calificación: F\n')

    # Imprima en pantalla al cantidad de ausentes
    print('\nEl Promedio del Alumno fue: {}'.format(promedio))
    print('\nLa Cantidad de Notas del Alumno sin Tener en cuenta los Ausentes son: {}'.format(cantidad_notas))
    print('\nLa Cantidad de Ausentes son: {}'.format(cantidad_ausentes))
    print('\nLa Suma de las Notas sin Tener en cuenta los Ausentes es: {}\n\n'.format(sumatoria))



def ej4():
    print("Mi primer pasito en Data Analytics:\n")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento

    En este ejercicio se lo provee de una lista de temperaturas,
    esa lista de temperaturas corresponde a los valores de temperaturas
    tomados durante una temporada del año en Buenos Aires.
    Usted deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo

    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados

    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperaturas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted.
    
    NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
    el máximo y el mínimo utilizando los mismos métodos vistos
    durante la clase (ejemplos_clase)
    '''

    temperatura_max = None      # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí almacenar el promedio
    temperatura_len = 0         # Aquí debe almacenar cuantas temperaturas hay en la lista

    # Colocar el bucle aqui......

    for i in range(len(temp_dataloger)):

        if ((temperatura_max is None) or (temperatura_max <= temp_dataloger[i])):
            temperatura_max = temp_dataloger[i]

        if ((temperatura_min is None) or (temperatura_min >= temp_dataloger[i])):
            temperatura_min = temp_dataloger[i]

        temperatura_sumatoria += temp_dataloger[i]



    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    print('\n\n1) La Temperatura Máxima es: {}'.format(temperatura_max))
    print('La Temperatura Máxima obtenida con la función "max" es: {}'.format(max(temp_dataloger)))

    print('\n2) La Temperatura Mínima es: {}'.format(temperatura_min))
    print('La Temperatura Mínima obtenida con la función "min" es: {}\n'.format(min(temp_dataloger)))



    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    temperatura_len = len(temp_dataloger)

    temperatura_promedio = temperatura_sumatoria / temperatura_len

    # Corrobore los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

    print('3) La Temperatura Promedio es: {}'.format(temperatura_promedio))
    print('La Temperatura Promedio obtenida con la función "sum" es: {}\n\n'.format(sum(temp_dataloger)/temperatura_len))

    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 24
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''

    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo

    invierno = [8, 14]
    otonio = [11, 24]
    primavera = [10, 24]
    verano = [19, 28]

    epoca_anio = None

    if ((invierno[0] <= temperatura_min <= invierno[1]) and (invierno[0] <= temperatura_max <= invierno[1])):
        epoca_anio = 'Invierno'

    elif ((otonio[0] <= temperatura_min <= otonio[1]) and (otonio[0] <= temperatura_max <= otonio[1])):
        epoca_anio = 'Otoño'

    elif ((primavera[0] <= temperatura_min <= primavera[1]) and (primavera[0] <= temperatura_max <= primavera[1])):
        epoca_anio = 'Primavera'

    elif ((verano[0] <= temperatura_min <= verano[1]) and (verano[0] <= temperatura_max <= verano[1])):
        epoca_anio = 'Verano'


    print('La Provincia de Buenos Aires se Encuentra en la Siguiente Época del Año: {}\n\n'.format(epoca_anio))


def ej5():
    print("Ahora sí! buena suerte :)\n\n")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?
    
    NOTA: No se debe ordenar la lista de palabras, se debe obtener
    el máximo utilizando el mismos métodos vistos durante la clase
    (ejemplos_clase), tal como el ejercicio anterior. Ordenar una
    lista representa un problema mucho más complejo que solo
    buscar el máximo.

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")

  '''

    # Inicialización de las Variables:

    palabras = [] # Lista Vacía
    max_palabra = None
    max_cant_letras = None

    flag = False  # Variable que Uso como Bandera

    while flag == False:

        print('Bienvenido/a:')
        print('¿Qué desea Realizar?\n')
        print('1 - Ordenar Palabras por Orden Alfabético (usando el operador ">")')
        print('2 - Ordenar Palabras por Cantidad de letras (longitud de la palabra)')
        print('3 - Salir del programa')
        opcion = int(input('\nIngrese a Continuación la Opción que Desee: '))

        if ((opcion == 1) or (opcion == 2)):

            cant_palabras_deseadas = int(input('\nIngrese el Nro. de Palabras que Desee Escribir: '))
            print('\n')

            while cant_palabras_deseadas > 0:
                palabra = str(input('Ingrese la Palabra que Desee: '))
                palabras.append(palabra)
                cant_palabras_deseadas -= 1

            if opcion == 1:
                for i in range(len(palabras)):
                    if ((max_palabra is None) or (max_palabra <= palabras[i])):
                        max_palabra = palabras[i]
                
                print('\n\nLa Mayor Palabra Más Grande Alfabéticamente es: "{}"\n\n'.format(max_palabra))


            if opcion == 2:
                for i in range(len(palabras)):
                    if ((max_cant_letras is None) or (len(max_cant_letras) <= len(str(palabras[i])))):
                        max_cant_letras = palabras[i]

                print('\n\nLa Palabra que Tiene Mayor Cantidad de Letras es: "{}"\n\n'.format(max_cant_letras))


        elif opcion == 3:
            flag = True
            print('\nEl Programa ha Finalizado.\n\n')


        else:
            print('\n¡¡¡¡ERROR!!!! Se ha Ingresado una Opción Inválida.\n\n')
            continue





if __name__ == '__main__':
    print("\nEjercicios de práctica.\n")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
