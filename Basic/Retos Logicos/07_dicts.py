'''
Ejercicio 1: Crear un Diccionario
Ejercicio 2: Crear un Diccionario con Información Personal
Ejercicio 3: Acceso a los Elementos del Diccionario
    Muestra el valor de la clave "Nombre".
    Muestra el valor de la clave "Programación".
    Intenta acceder a la clave "Dirección" (que no existe) 

Ejercicio 4: Comprobar si una Clave Existe

Comprueba si las claves "Edad" y "Teléfono" existen en el diccionario creado en el ejercicio 2.
Usa el operador in y muestra el resultado

Ejercicio 5: Modificar un Valor de un Diccionario

Ejercicio 6: Añadir Nuevas Claves
Añade una nueva clave "Email" al diccionario con el valor "ana@example.com".
Luego imprime el diccionario actualizado.

Ejercicio 7: Eliminar una Clave

Ejercicio 8: Métodos del Diccionario
Muestra todos los elementos del diccionario con items().
Muestra solo las claves del diccionario con keys().
Muestra solo los valores del diccionario con values().

Ejercicio 9: Crear un Diccionario a partir de una Lista
¡Claro! Aquí tienes una serie de ejercicios prácticos sobre Diccionarios en Python, basados en el código de la clase que me proporcionaste. Los ejercicios cubren diversos aspectos de los diccionarios, como la creación, acceso, actualización, eliminación y otras operaciones.
Ejercicio 1: Crear un Diccionario

Crea un diccionario vacío usando dos formas diferentes:

    Usando dict()
    Usando las llaves {}

Muestra el tipo de ambos diccionarios con type().
Ejercicio 2: Crear un Diccionario con Información Personal

Crea un diccionario con la siguiente información de una persona:

    Nombre: "Ana"
    Apellido: "González"
    Edad: 28
    Ciudad: "Madrid"
    Programación: {"Python", "JavaScript", "Java"}

Luego, imprime el diccionario y muestra su longitud con len().
Ejercicio 3: Acceso a los Elementos del Diccionario

Usando el diccionario que creaste en el ejercicio anterior, realiza las siguientes operaciones:

    Muestra el valor de la clave "Nombre".
    Muestra el valor de la clave "Programación".
    Intenta acceder a la clave "Dirección" (que no existe) y maneja el error con un try-except.

Ejercicio 4: Comprobar si una Clave Existe

Comprueba si las claves "Edad" y "Teléfono" existen en el diccionario creado en el ejercicio 2.
Usa el operador in y muestra el resultado.
Ejercicio 5: Modificar un Valor de un Diccionario

En el diccionario que creaste en el ejercicio 2:

    Cambia el valor de "Edad" a 29.
    Imprime el diccionario después de realizar la modificación.

Ejercicio 6: Añadir Nuevas Claves

Añade una nueva clave "Email" al diccionario con el valor "ana@example.com". Luego imprime el diccionario actualizado.
Ejercicio 7: Eliminar una Clave

Elimina la clave "Ciudad" del diccionario y muestra el diccionario resultante. Utiliza del para hacerlo.
Ejercicio 8: Métodos del Diccionario

Usando el diccionario creado en el ejercicio 2, realiza lo siguiente:

    Muestra todos los elementos del diccionario con items().
    Muestra solo las claves del diccionario con keys().
    Muestra solo los valores del diccionario con values().

Ejercicio 9: Crear un Diccionario a partir de una Lista

Usa la lista ["Nombre", "Apellido", "Edad"] para crear un nuevo diccionario con valores por 
defecto de None usando el método fromkeys(). Imprime el diccionario.

Ejercicio 10: Crear un Diccionario con un Valor Común

Ejercicio 12: Convertir un Diccionario a Otros Tipos

Convierte el diccionario que creaste en el ejercicio 2 a:

    Una tupla.
    Un conjunto.

Muestra ambos resultados.
'''

#1 y 2
my_dict = dict()
my_new_dict = { 'Nombre': 'Santiago', 
                'Apellido': 'Gaviria',
                'Telefono' : 3137863327,
                'Correo': 'sgaviria@uc.edu.co'}

'''Ejercicio 3: Acceso a los Elementos del Diccionario
    Muestra el valor de la clave "Nombre".
    Muestra el valor de la clave "Programación".
    Intenta acceder a la clave "Dirección" (que no existe) '''

print(my_new_dict['Nombre'])
print(my_new_dict['Telefono'])


'''Ejercicio 4: Comprobar si una Clave Existe
Comprueba si las claves "Edad" y "Teléfono" existen en el diccionario creado en el ejercicio 2. 
Usa el operador in y muestra el resultado.'''

print('Nombre' in my_new_dict)
print('Telefono' in my_new_dict)

#05 Actualizar
my_new_dict['Nombre'] = 'Roberto'
print(my_new_dict['Nombre'])

#06 Insertar
my_new_dict['Edad'] = 21
print(my_new_dict)

#07 Eliminar
del my_new_dict['Telefono']
print(my_new_dict)
'''
Ejercicio 8: Métodos del Diccionario
    Muestra todos los elementos del diccionario con items().
    Muestra solo las claves del diccionario con keys().
    Muestra solo los valores del diccionario con values().
'''
my_dict = my_new_dict.copy()
print(my_new_dict.items())
print(my_new_dict.keys())
print(my_new_dict.values())

#9  
my_list = ['Lenguaje', 'Alumno', 'Semillero']
my_dict = dict.fromkeys(my_list)
print(my_dict)

#10
my_new_dict = dict.fromkeys(my_dict, 'desconocido')
print(my_new_dict)

#11 

my_tuple = tuple(my_dict)
print(my_tuple)

my_list = list(my_dict)
print(my_list)

my_set = set(my_dict)
print(my_set)
