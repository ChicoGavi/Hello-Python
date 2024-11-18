# 1. Declara y asigna valores a las siguientes variables:
# â€¢	name: una cadena que contenga tu nombre.
# â€¢	age: un nÃºmero entero que represente tu edad.
# â€¢	height: un nÃºmero flotante que represente tu altura.
# â€¢	Imprime cada variable en una lÃ­nea separada.

# 2. Convierte la variable edad de entero a string y concatenala con un texto que diga cuÃ¡ntos aÃ±os tienes.

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False segÃºn corresponda e imprÃ­mela.

# 4. Usa la funciÃ³n len() para calcular cuantos caracteres tiene tu nombre completo, almacenado en una variable.

# 5. Declara tres variables en una sola lÃ­nea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.

# 6. Usa la funciÃ³n input() para solicitar al usuario su color favorito y almacÃ©nalo en una variable color. Luego, imprime el valor ingresado.

# 7. Declara una variable fruit e inicialÃ­zala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.

# 8. Convierte un nÃºmero decimal, almacenado en la variable price, a un nÃºmero entero y luego imprÃ­melo.

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una direcciÃ³n usando la funciÃ³n len(). Imprime el resultado.

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurÃ¡ndote de que siempre serÃ¡ un nÃºmero. Luego, cambia su valor a un nÃºmero diferente y verifica el tipo de la variable con type().

#1
name = 'Santiago'
age = 21
height = 1.78

print(name)
print(age)
print(height)

#2:
print('Su edad es: ' + str(age))

# 3
is_student = input('Es usted un estudiante, reponsa si o no: ').lower()
if is_student == 'si':
    print(True)
elif is_student == 'no':
    print(False)
else:
    print('No corresponde, por favor digite nuevamente: ')

# 4.

my_name = len(input('Digite su nombre: '))
print(my_name)

# 5.
name, city, surname = input('Digite su nombre: '), input('Digite su ciudad: '), input('Digite su apellido')
print(f'Hola a todos, mi nombre es {name}, con mi apellido de padre{surname} y vivo actualmente en la ciudad de {city}')

#6
color_client = input('Cual es su color que desea llevar?: ')
print(f'El cliente desea llevar el siguiente color: {color_client}')

#7: 
fruit = 'Pera'
print(fruit)
print(type(fruit))

fruit = 15
print(fruit)
print(type(fruit))

#8:
price = 59.99
print(price)
print(type(price))

price = 60
print(price)
print(type(price))

#9
address_len = input('Digite su direccion: ')
print(f'Su direccion es la siguiente: {address_len} y la cantidad de caracteres es de {len(address_len)}')

#10
phone:int = 3137863327 
print(f'Su numero de celular es: {phone} y su tipo de dato es: {type(phone)}')

phone:int = 3.1516
print(f'Su numero de celular es: {phone} y su tipo de dato es: {type(phone)}')