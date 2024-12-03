#Realice una función para dibujar un rectángulo con el carácter que el usuario
#  elija también debe pedirle al usuario las medidas del rectángulo, 
# este ejercicio se hace de manera similar que los triángulos que ya hemos trabajado.

class rectangulo: 
    def __init__(self):
        self.caracter = input('Ingrese un caracter: ')
        self.alto = int(input('Ingrese la longitud de caracter: '))
        self.ancho = int(input('Ingrese el ancho del rectangulo '))
    
    def ecuacion(self):
        i = 0
        while i < self.alto:
            print(self.caracter * self.ancho)
            i+= 1


matematicas = rectangulo()

matematicas.ecuacion()

