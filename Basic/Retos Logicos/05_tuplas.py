#1 Ejercicio 1: Creación y acceso
#    Crea una tupla colors con los valores: "rojo", "verde", "azul", "amarillo".
#       Imprime el segundo color.
#      Imprime el último color usando un índice negativo.
#      Intenta cambiar el tercer color por "morado" y observa el error.

'''Ejercicio 2: Búsqueda en tuplas

    Crea una tupla numbers con los valores: (5, 10, 15, 10, 20, 10, 25).
        Imprime cuántas veces aparece el número 10.
        Encuentra el índice de la primera aparición del número 20.
        ¿Qué ocurre si intentas buscar un número que no está en la tupla? Inténtalo.'''

'''
Ejercicio 3: Concatenación

    Crea dos tuplas:
        tuple1 con los valores: (1, 2, 3)
        tuple2 con los valores: (4, 5, 6)
        Concáténalas y almacena el resultado en result_tuple.
        Imprime result_tuple.
        Accede al cuarto elemento de la tupla resultante
'''

'''
Ejercicio 4: Subtuplas y slicing

    Dada la tupla alphabet = ("a", "b", "c", "d", "e", "f", "g", "h"):
        Extrae una subtupla con los elementos desde el segundo hasta el quinto.
        Extrae los elementos desde el inicio hasta el tercer elemento.
        Extrae todos los elementos con un paso de 2.
        Invierte la tupla usando slicing.
'''

'''
Ejercicio 5: Conversión y modificación

    Dada la tupla fruits = ("manzana", "naranja", "plátano"):
        Convierte la tupla en una lista.
        Cambia el segundo elemento a "kiwi".
        Agrega "mango" al final de la lista.
        Convierte la lista nuevamente en tupla y muéstrala.
'''
'''
Ejercicio 6: Comparación de tuplas

    Dadas las tuplas tuple_a = (1, 2, 3) y tuple_b = (1, 2, 4):
        Compara ambas tuplas usando == y muestra el resultado.
        ¿Qué ocurre si usas el operador < o >? Inténtalo y analiza.
'''
'''
Ejercicio 7: Empaquetado y desempaquetado

    Dada la tupla person = ("Santiago", 21, "Colombia"):
        Desempaqueta los valores de la tupla en las variables name, age, y country.
        Imprime los valores de las variables.
        Usa el operador * para desempaquetar los elementos en una variable llamada details, dejando el primer elemento como name.

'''

'''
Ejercicio 8: Tuplas anidadas

    Crea una tupla anidada nested_tuple = (1, (2, 3), (4, (5, 6))):
        Accede al valor 3.
        Accede al valor 5.
        Intenta modificar el valor 3 por 10 y explica el resultado
'''
'''
Ejercicio 10: Longitud de tuplas

    Crea una tupla random_tuple = (1, "Hola", True, 3.14, "Python").
        Imprime la longitud de la tupla usando len().
        ¿Qué ocurre si intentas agregar un nuevo elemento?
'''

#1 Ejercicio 1: Creación y acceso

colors = ('red','white','black','yellow')
print(colors[1])
print(colors[-1])
#colors[2] = 'pink'   # ERROR: Dont support item assignment

'''Ejercicio 2: Búsqueda en tuplas'''

numbers = (5,10,15,20,10,25,20)
print(numbers.count(10))
print(numbers.index(20))

#print(numbers.index(30))  ERROR: tuple.index(x) not in tuple

'''
Ejercicio 3: Concatenación
'''

first_tuple = (17,18,19)
second_tuple = (20,21,22)
result_tuple = first_tuple + second_tuple
print(result_tuple)
print(result_tuple[3])

'''
Ejercicio 4: Subtuplas y slicing
'''
alphabet = ("a", "b", "c", "d", "e", "f", "g", "h")
small = alphabet[1:5]
print(small)
print(alphabet[0:3])
print(alphabet[::2])
print(alphabet[::-1])

'''
Ejercicio 5: Conversión y modificación
'''
fruits = ('apple','banana','orange')
fruits = list(fruits)
fruits[1] = 'Kiwi'
fruits.append('mango')
fruits = tuple(fruits)
print(fruits)

'''
Ejercicio 6: Comparación de tuplas'''
tuple_a = (1,2,3)
tuple_b = (1,2,4)

print(tuple_a == tuple_b)
print(tuple_a > tuple_b)
print(tuple_a < tuple_b)

'''
Ejercicio 7: Empaquetado y desempaquetado
'''

my_person = ('Santiago', 21, 'Pereira', 'Colombia')
name, age, city, country = my_person
print(age)

name, *details = my_person
print(details)

