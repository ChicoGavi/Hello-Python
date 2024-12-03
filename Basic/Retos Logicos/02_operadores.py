# 1. Realiza las siguientes operaciones aritmÃ©ticas:
# â€¢	Suma: 15 + 25
# â€¢	Resta: 50 - 22
# â€¢	MultiplicaciÃ³n: 8 * 7
# â€¢	DivisiÃ³n: 100 / 20

# 2. Calcula el resto de la divisiÃ³n de 37 entre 5 
# y almacÃ©nalo en una variable remainder. 
# Luego imprÃ­melo.

# 3. Convierte el nÃºmero 7 en una cadena de texto y concatÃ©nalo con la frase â€œ es mi nÃºmero favoritoâ€. 
# Imprime el resultado.

# 4. Repite la palabra â€œPythonâ€ 10 veces usando el operador de multiplicaciÃ³n para cadenas y luego imprÃ­mela.

# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.

# 6. Compara dos cadenas de texto (â€œappleâ€ y â€œbananaâ€) usando los operadores > y < y explica cuÃ¡l tiene mayor orden alfabÃ©tico.

# 7. Realiza una comparaciÃ³n lÃ³gica usando and para verificar si el nÃºmero 10 es mayor que 5 y menor que 20. Imprime el resultado.

# 8. Usa el operador or para verificar si el nÃºmero 7 es menor que 3 o mayor que 5. Imprime el resultado.

# 9. Aplica el operador not para invertir el resultado de la comparaciÃ³n 15 > 20. Â¿CuÃ¡l es el resultado?

# 10. Combina operadores aritmÃ©ticos y lÃ³gicos: Verifica si el nÃºmero resultante de la expresiÃ³n (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado


#1: 
suma = 15 + 25
resta = 50 - 22
multiplicacion = 8 * 7
division = 100/20




#2 

remainder = 37 % 5 
print(f'El resto de la division de 37/5 es: {remainder}')

#3 
numero = int(input('Por favor, digite un numero: '))
print(f'Este es mi numero favorito {numero}')
print('Este es mi numero favorito: ' + str(numero))

#4
#4.1
lenguaje = ' Python ' * 2
print(f'Mi lenguaje favorito es {lenguaje}')

#4.2
lenguaje_dos = input('Este es mi lenaguaje favorito: ' ) * 2
print('Este es mi lenguaje favorito ' + (lenguaje_dos))

#4.3
lenguaje_tres = 'GO'
print(f'Mi lenguaje favorito es: {lenguaje_tres * 2}')

#5
a = 12
b = 8
resultado = a > b  
print(resultado)

a = input('Por favor digite un numero: ')
b = input('Por favor Digite otro numero: ')
resultado = a > b 
print(f'El valor de {a} es mayor que {b}')

#6
fruta_uno = 'apple' > 'banana'
fruta_dos = 'apple' < 'banana'
resultado = print(f'El primer valor: {fruta_uno} se evidencia que apple es menor que banana {fruta_dos}')


print('apple' > 'banana')
print('apple' < 'banana')

#7
logica = 10 > 5 and 10 < 20
print(10 > 5 and 10 < 20)
print(logica)
print(f'Si se esta cumpliendo los valores, {logica}')

#8
logica_dos = 7 < 3 or 7 > 5
print(logica_dos)
print(7 < 3 or 7 > 5)

#9
use_not = not(15 > 20)
print(f'Lo contrario seria: {use_not}')

log_not = 15 > 20
print(f'Lo contrario seria: {not(use_not)}')

#10
aritmethic = ((5*3)+2) > 10 and ((5*3)+2) < 20
print(aritmethic)

operation = (5*3)+2
print(operation > 10 and operation < 20)

print(((5*3)+2) > 10 and ((5*3)+2) < 20)

valor_uno, valor_dos, valor_tres = input('Digite un numero: '), input('Digite otro numero: '), input('Digite un numero')
print(((valor_uno*valor_dos)+valor_tres) > 10 and ((valor_uno*valor_dos)+valor_tres) < 20)