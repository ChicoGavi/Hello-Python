# 1. Imprime Hola mundo por consola
# 2. Escribe un comentario de una sola lÃ­nea explicando
#  quÃ© hace el cÃ³digo del Ejercicio 1
#3. Imprime tu nombre y edad en la misma lÃ­nea utilizando la funciÃ³n print
#4. Usa la funciÃ³n type() para imprimir el tipo de dato de una cadena de texto, un nÃºmero entero y un nÃºmero decimal.
#5. Escribe un comentario en varias lÃ­neas explicando quÃ© son los tipos de datos en Python
# 6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".
# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma lÃ­nea.
# 8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.
# 9. Usa print() para mostrar el resultado de la suma de dos nÃºmeros enteros y el tipo de dato resultante.
# 10. Comenta el cÃ³digo del Ejercicio 9, y explica quÃ© hace cada lÃ­nea usando comentarios de una sola lÃ­nea.


#1:
print("Hola mundo")

#2:
#En la linea anterior, se imprime por consola el mensaje "Hola mundo"

#3: 
print('Mi nombre es Santiago y', ' Mi edad es 21 years')

#4:
print(type('Mi nombre es Santiago y' + ' Mi edad es 21 years'))
print(type(21))
print(type(3.1416))

#5: 
'''
En Python, los tipos de datos son la cantidad de datos que se pueden asignar a variables, como lo son:
        1. Entero
        2. Float 
        3. String
        4. Boolean
        5. Number Complex 
'''

#6 
print("Hola "  + " mundo")

#7
name = 'Santiago'
age = 21
print(f'Mi nombre es: {name} y mi edad es de: {age} anos')

#8 
name = input('Cordial saludo Por favor, digite su nombre: ')

#9 
print(type(print(5+10)))
print(5+10)
print(type(5+10))
