### Haz un menu de plantas de un vivero
# 1 Catalogo Plantas / Listo
# 2 Nombre vendedor / Listo
# Nombre cliente /Listo
# 3 Factura de compra 
# 4 Si es cliente o provedor por cedula o Nit
# 5 Si es a domicilio o recoge 
# 6 Cantidad de plantas a llevar 
# 7 En efectivo o a credito 
# A credio a cuantas cuotas
# Sumarle el IVA del 18% al precio final 

class Vivero: 
    def __init__(self) :
        # Inicializando atributos de la instancia
        self.catalogo = 0
        self.nombre_vende = 'Santiago G'
        self.nombre_cliente = input('Digite su nombre: ')
        self.orquideas = 0
        self.cantidad_plantas = 0
        self.venta = 0



        self.factura = 0
        self.documento = ' '
        self.modo_entrega = 1
        
        self.modo_venta = 0
        self.cuotas = 0
        self.iva = 0.19


    def proceso_venta(self):
            print(f'Bienvenidos al Vivero Maracay, soy {self.nombre_vende}')
            print(f'Mucho gusto, {self.nombre_cliente}')
        
            self.catalogo = int(input('''Desea comprar o salir? 
                    1. Ingresar al menu de plantas
                    0. Salir'''))

            
            
            match self.catalogo:
                        case 1:
                            while self.catalogo != 0:
                                self.catalogo = int(input('''
                                1. Orquideas 
                                2. Bonsais 
                                3. Suculentas
                                4. Arboleas
                                5. Frutales
                                0. Salir'''))
                                match self.catalogo:
                                    case 1: 
                                        self.venta = int(input('''Que tipo de Orquidea prefiere: 
                                            1. Catleya $5000
                                            2. Benedicta $ 10000
                                            3. Arroya $15000
                                            0. Salir'''
                                                    ))
                                        
                                        match self.venta:
                                            case 1:
                                                print('Eligio Catleya por un valor de 5000')
                                                self.cantidad_plantas += self.venta
                                                print(self.cantidad_plantas)
                                            case 2:
                                                print('Eligio Benedicta por un valor de 10.000')
                                                self.cantidad_plantas += self.venta
                                                print(self.cantidad_plantas)
                                            case 3: 
                                                print('Eligio Arroya por un valor de 15.000')
                                                self.cantidad_plantas += self.venta
                                                print(self.cantidad_plantas)
                                    case 2:
                                        pass
                
                

Plantas = Vivero()
Plantas.proceso_venta()
        

