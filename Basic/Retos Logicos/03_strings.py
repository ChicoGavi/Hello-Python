##Longitud de una cadena: Crea una variable 
# greeting con el valor "¡Hola Mundo!" 
# Imprime la longitud de la cadena greeting.

#2 Concatenación de cadenas:Crea dos variables: city = "Madrid" y country = "España".
# Concatena ambas variables con un espacio entre ellas y luego imprímelas.

#3
#Uso de salto de línea y tabulación:Crea una variable message con el valor "Primera línea\nSegunda línea" 
# y luego imprímela. Crea otra variable tab_message con el valor "\tTexto con tabulación" y luego imprímela.

#4Crea tres variables: first_name = "Carlos", last_name = "Pérez", y age = 28.
#Usa el método .format(), el formateo con %, y f-strings para imprimir la frase:
#  "Mi nombre es Carlos Pérez y tengo 28 años".

#5. Desempaquetado de caracteres: Crea una variable word = "mango".
# Desempaqueta los caracteres de la cadena en variables y luego imprime las primeras y últimas letras de la palabra.

#6 Crea una variable fruit = "sandía".
#Usa slicing para obtener y imprimir:
#Los caracteres del índice 2 al 4.
#Los caracteres desde el índice 1 hasta el final.
#El penúltimo carácter.
#Los caracteres desde el inicio con un paso de 2.

#7 Crea una variable reverse_example = "python".
#Imprime la versión invertida de la cadena utilizando el slicing adecuado

#8 Crea una variable sentence = "hola mundo".
#Usa y imprime los resultados de los siguientes métodos:
#capitalize()
#upper()
#count("o")
#isnumeric() (para verificar si la cadena es un número)
#lower()
#Verifica si la cadena en minúsculas es igual a la cadena en mayúsculas usando isupper().
#Usa startswith("ho") para verificar si la cadena empieza con "ho".

#9 Crea dos variables: text1 = "hola" y text2 = "Hola".
#Compara las dos cadenas usando == y explica por qué el resultado es falso

#1 
greeting = len('hola mundo')
print(greeting)

#greeting = len(input('Digite hola mundo: '))
#print(len(greeting))

#2 
city = 'Madrid'
country = 'Espana'
print(city + ' '+country)

city, country = 'Madrid', 'Espana'
print(f'Su ciudad natal es \t {city} \n y su pais de natalidad es: {country}')

#3 
print('Mi nombre es Santiago Y soy estudiante de programacion de la Universidad CIAF \n.\t Tambien soy estudiante de administracion en sistemas en la Universidad de comfamiliar')

#4 
my_name = 'Santiago'
surname = 'Gaviria'
age = 21
print(f'Mi nombre es {my_name} y mi apellido es {surname} y tengo {age} anos')

#full_name = input('Digite por favor su nombre completo: ')
#age = input('Digite su edad: ')
#print('Mi nombre es %s y tengo de edad la siguiente %s' % (full_name, age))
#print('Mi nombre es {} y tengo {} anos '.format(full_name, age))

#5 
fruit = 'Mango'
a, b, c, d, e = fruit
print(a,b,c)
print(d,e)

#6
access_fruit = 'PineApple'

random = access_fruit[3::]
print(random)

#7
word = 'Java'
word_reverse = print(word[::-1])

#word = input('Ingrese su lenguaje de programacion favorito: ')
#print(word[::-1])

#8 
iputty = input('Ingrese su framework favorito: ')
print(iputty.upper())
print(iputty.lower())
print(iputty.capitalize())
print(iputty.count('e'))
print(iputty.islower())
print(iputty.isupper())
print(iputty.endswith('x'))
print(iputty.replace('reflex', 'Django'))

surname = ' Gaviria '
prueba_join = ['Roberto', 'Alvaro', 'Final']
resultado = surname.join(prueba_join)
print(resultado)

#Convierte en una lista
print(resultado.split(' ',2))

