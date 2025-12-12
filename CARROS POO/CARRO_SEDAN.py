from CODIGO_GENERAL import Carro

class Carros_sedanes(Carro):
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
        
