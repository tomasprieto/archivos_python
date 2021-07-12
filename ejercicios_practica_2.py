# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    stock = open('stock.csv')
    lista = []
    lista_2 = []
    data = list(csv.DictReader(stock))
    

    for i in data:
        lista.append(i['tornillos'])
    
    for num in lista:         
        num = int(num) 
        lista_2.append(num)
        
    
    total = sum(lista_2)
    print('total en la columna "tornillos":', total)
    stock.close()

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    propiedades = open('propiedades.csv')
    
    data = list(csv.DictReader(propiedades))

    lista = []

    for i in data:
        try:
            lista.append(i['ambientes'])
        except:
            continue

    cantidad_2_amb = lista.count('2')
    cantidad_3_amb = lista.count('3')

    print('Cantidad de 2 ambientes:', cantidad_2_amb)
    print('Cantidad de 3 ambientes:', cantidad_3_amb)

    propiedades.close()




if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
