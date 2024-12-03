#1: Crea una lista con los elementos ["manzana", "banana", "cereza"].
#Imprime la longitud de la lista usando len().

#2: Crea dos listas: Combina ambas listas y guarda el resultado en una nueva lista.
# Imprime la lista combinada.

#3: Dada la lista animals = ["perro", "gato", "loro"]:
#Cambia el segundo elemento de la lista por "tigre". Imprime la lista modificada.

#4: Crea una lista de tres cadenas: ["Primera línea", "Segunda línea", "Tercera línea"].
# Imprime cada elemento de la lista en una nueva línea usando un bucle.

#5: Crea una lista numbers = [10, 20, 30, 40, 50].
#Usa desempaquetado para asignar el primer, segundo y último elemento de la lista a variables separadas.
# Imprime las variables.

#6: Crea una lista colors = ["rojo", "verde", "azul", "amarillo", "negro"].
#Obtén e imprime los elementos del índice 1 al 3.
#Imprime la lista desde el inicio hasta el índice 3 (sin incluirlo).
#Imprime los elementos en orden inverso.

#7: Crea una lista letters = ["a", "b", "c", "d", "e"].
#Invierte la lista usando slicing y el método .reverse().
#Imprime ambas versiones.

#8: Crea una lista numbers = [1, 2, 3, 4, 5, 3].
#Usa e imprime los resultados de los siguientes métodos:
#   append() para agregar un número.
#   remove() para eliminar un número específico.
#   count() para contar cuántas veces aparece un número.
#    index() para obtener la posición de un número.

#9: Crea dos listas: list1 = [1, 2, 3] list2 = [1, 2, 3]
#Compara ambas listas con == y is.
#Explica la diferencia entre ambas comparaciones.

#10: Crea una cadena text = "Hola, Mundo, Python".
#Convierte la cadena en una lista de palabras usando .split().
#Une la lista en una cadena separada por guiones usando .join().

#1 
fruits = ['banano', 'manzana', 'pera', 'sandia']
print(len(fruits))

fruits = print(['banano', 'manzana', 'pera', 'sandia'])

#fruits = [input('Digite una lista de frutas: ')]
#print(fruits)


#2
list_one = [10,20,30,40]
list_two = [1,2,3,4]
print(list_one + list_two)

result = list_one + list_two
print(result) 

#list_one = [input('Digite los valores de la primera lista: ')]
#list_two = [input('Digite los valores de la segunda lista: ')]
#print(list_one + list_two)

#3 
animals = ['Elephant','Tiger','Cat']
print(animals)

animals[1] = 'Dog'
print(animals)

#animals = [input('Digite los animales separados por una coma, : ')]
#print(len(animals))

#4: Crea una lista de tres cadenas: ["Primera línea", "Segunda línea", "Tercera línea"].
# Imprime cada elemento de la lista en una nueva línea usando un bucle.

my_list = ['Santiago','Erazo','Diego']
for i in my_list:
    print(i[0:3])
    print(i[-5::])

#5: Crea una lista numbers = [10, 20, 30, 40, 50].
#Usa desempaquetado para asignar el primer, segundo y último elemento de la lista a variables separadas.
# Imprime las variables.

apeliidos = ['Gaviria', 'Castro', 'Santiago', 'Roberto', 'Felipe']
apellido, *omitir, apellido_dos, nombre = apeliidos
print(omitir)

#6: Crea una lista colors = ["rojo", "verde", "azul", "amarillo", "negro"].
#Obtén e imprime los elementos del índice 1 al 3.
#Imprime la lista desde el inicio hasta el índice 3 (sin incluirlo).
#Imprime los elementos en orden inverso.

colors = ['rojo', 'verde', 'amarillo', 'verde', 'azul']
print(colors[0:3])
print(colors[::-1])

#7: Crea una lista letters = ["a", "b", "c", "d", "e"].
#Invierte la lista usando slicing y el método .reverse().
#Imprime ambas versiones.

letters = ['a','b','c','d']
print(letters[::-1])

letters.reverse()
print(letters)

#8: Crea una lista numbers = [1, 2, 3, 4, 5, 3].
#Usa e imprime los resultados de los siguientes métodos:
#   append() para agregar un número.
#   remove() para eliminar un número específico.
#   count() para contar cuántas veces aparece un número.
#    index() para obtener la posición de un número.
numbers = [1,2,3,4,5,6,8,8]
numbers.append(198)
print(numbers)

numbers.count(8)
print(numbers)

numbers.remove(8)
print(numbers)

print(numbers.index(3,0))

new_numbers = numbers.copy()
#numbers.clear()
print(new_numbers)

new_numbers.extend(numbers)
print(new_numbers)

new_numbers.sort()
print(new_numbers)

stril = 'Santiago'
resultado = stril.join(letters)
print(resultado)

#9: Crea dos listas: list1 = [1, 2, 3] list2 = [1, 2, 3]
#Compara ambas listas con == y is.
#Explica la diferencia entre ambas comparaciones.
list_one = [1,2,3,4] 
list_two = [1,2,3,4]

print(list_one == list_two)
print(list_one is list_two)

#==: Compara los contenidos (equivalencia lógica).
#is: Compara las referencias (identidad en memoria).