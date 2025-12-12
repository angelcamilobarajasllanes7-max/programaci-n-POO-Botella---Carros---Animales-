from CODIGO_GENERAL import Carro
class Carros_SUVs(Carro):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
        
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible
        
    def Imprimir_datos(self):
        print(f'modelo: {self.modelo}')
        print(f'color: {self.color}')
        print(f'motor: {self.motor}')
        print(f'numero de puertas: {self.numero_puertas}')
        print(f'capacidad de pasajeros: {self.capacidad_pasajeros}')
        print(f'tipo de combustible: {self.tipo_combustible}')
        
        
        
    def Arranque(self):
        print("hacia adelante\n")
        
    def Apagado(self):
        print("se gira la llave y automaticamente se apaga\n")
        
    def Aceleracion_y_frenado(self):
        print("aceleracion de 0 a 100 en 20sg y frenado inmediato\n")
        
    def Sistema_direccion(self):
        print("volante redondo con su diseño exclusivo\n")
        
    def Climatizacion(self):
        print(" tiene un sistema de aire frio o caliente\n")
        
    def Tipo_seguridad(self):
        print("muy seguro anti robos\n")
        
    def Luces(self):
        print("luces con 200 voltios\n")
        
    def Sistema_ventanas(self):
        print("grosor de vidrio ventanales son de 9,0mm\n")
        
    def Sistema_espejo(self):
        print("tiene espejos en el lado derecho como izquierdo\n\n")

