'''Ejercicio 1: Crear y agregar elementos a un set

    Crear un set vacío.
    Agregar los elementos "rojo", "verde" y "azul" al set.
    Intentar agregar un elemento repetido y observar el resultado.'''

'''
Ejercicio 2: Búsqueda en un set

    Crear un set con los números {1, 2, 3, 4, 5}.
    Verificar si el número 3 está en el set.
    Verificar si el número 6 no está en el set.
'''

'''
Ejercicio 3: Eliminar elementos de un set

    Crear un set con los nombres {"Juan", "Ana", "Carlos"}.
    Eliminar "Ana" del set.
    Intentar eliminar un elemento inexistente con remove (provoca error).
    Eliminar un elemento inexistente con discard (no provoca error).
'''
'''
Ejercicio 4: Operaciones de conjuntos

    Crear dos sets: set_a = {1, 2, 3} y set_b = {3, 4, 5}.
    Obtener la unión, intersección y diferencia entre ambos sets.


'''
'''
Ejercicio 5: Conversión entre tipos

    Convertir una lista con elementos repetidos en un set para eliminar duplicados.
    Convertir el set resultante de vuelta en una lista.
'''

'''Ejercicio 6: Comparación de sets

    Crear dos sets: set_x = {1, 2, 3} y set_y = {1, 2}.
    Comprobar si set_y es un subconjunto de set_x.
    Comprobar si set_x es un superconjunto de set_y.

'''
'''
Ejercicio 8: Vaciar y eliminar sets

    Crear un set con los elementos {"a", "b", "c"}.
    Vaciar el set con el método clear.
    Eliminar el set completamente con del
'''

'''
Ejercicio 9: Duplicar elementos al unir sets

    Crear dos sets con elementos comunes: set_p = {1, 2, 3} y set_q = {3, 4, 5}.
    Unir ambos sets y verificar que no hay duplicados.

'''

'''Ejercicio 1: Crear y agregar elementos a un set'''

my_set = {}
my_set = {'red','green','blue','blue'}   #No acepta valores repetidos
print(my_set)

'''Ejercicio 2: Búsqueda en un set  
'''
numeric = {1,2,3,4,5,6,7,8,9}
print(3 in numeric)  
print(10 not in numeric) #Verificar si el número 10 no está en el set.

'''
Ejercicio 3: Eliminar elementos de un set

'''
names = {'Santiago','Erazo','Diego'}
names.discard('Luisa') #Elimina un elemento del set, asi no este definido en el set
names.remove('Erazo')#Elimina un elemento del set, tiene que estar definido en el set
print(names)

'''
Ejercicio 4: Operaciones de conjuntos
'''

set_a = {9,8,7,6}
set_b = {6,5,4}

set_c = {21,58,4}

print(set_a.union(set_b))
print(set_b.intersection(set_a))   # Lo que tienen en comun ambos set
print(set_c.difference(set_b,set_a))  # Lo diferente que ahi en un set que no esta en los demas set


'''
Ejercicio 5: Conversión entre tipos
    Convertir una lista con elementos repetidos en un set para eliminar duplicados.
    Convertir el set resultante de vuelta en una lista.
'''

list_one = [5,5,5,2,2,2,1,1,1]
my_set_list = set(list_one)
print(my_set_list)

list_one = list(my_set_list)
print(list_one)
