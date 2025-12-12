class Carro():
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
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
        print("hacia adelante")
        
    def Apagado(self):
        print("sin gasolina se apaga")
        
    def Aceleracion_y_frenado(self):
        print("aceleracion 0sg y frenado inmediato")
        
    def Sistema_direccion(self):
        print("volante redondo")
        
    def Climatizacion(self):
        print("aire frio o caliente")
        
    def Tipo_seguridad(self):
        print("muy seguro anti robos")
        
    def Luces(self):
        print("luces con 100 voltios")
        
    def Sistema_ventanas(self):
        print("grosor de vidrio ventanales son de 8,0mm")
        
    def Sistema_espejo(self):
        print("tiene espejos en lado derecho como izquierdo")
        
        
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
        
        
        
    def Arranque(self):
        print("hacia adelante\n")
        
    def Apagado(self):
        print("se gira la llave y automaticamente se apaga\n")
        
    def Aceleracion_y_frenado(self):
        print("aceleracion de 0 a 100 en 50sg y frenado inmediato\n")
        
    def Sistema_direccion(self):
        print("volante redondo con su diseño exclusivo\n")
        
    def Climatizacion(self):
        print(" tiene un sistema de aire frio o caliente\n")
        
    def Tipo_seguridad(self):
        print("muy seguro anti robos\n")
        
    def Luces(self):
        print("luces con 100 voltios\n")
        
    def Sistema_ventanas(self):
        print("grosor de vidrio ventanales son de 8,0mm\n")
        
    def Sistema_espejo(self):
        print("tiene espejos en el lado derecho como izquierdo\n\n")
        
        
        
        
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

        
        
        
class Carros_coupes(Carro):
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
        print("aceleracion de 0 a 100 en 1sg y frenado inmediato\n")
        
    def Sistema_direccion(self):
        print("volante redondo con su diseño exclusivo con botones para abrir las puertas del carro\n")
        
    def Climatizacion(self):
        print(" tiene un sistema de aire frio o caliente\n")
        
    def Tipo_seguridad(self):
        print("muy seguro anti robos\n")
        
    def Luces(self):
        print("luces con 230 voltios\n")
        
    def Sistema_ventanas(self):
        print("anti balas\n")
        
    def Sistema_espejo(self):
        print("tiene espejos en el lado derecho como izquierdo\n\n")

        

        

## CODIGO PRINCIPAL

## CARROS SEDANES
print("INFORMACION DE LOS CARROS SEDANES\n\n")
Obj_carro_sedanes = Carros_sedanes('123 2018\n', 'negro\n', '8 caballos de fuerza\n', '4 puertas\n', '5 pasajeros\n', 'gasolina\n\n')
Obj_carro_sedanes.Imprimir_datos()
Obj_carro_sedanes.Arranque()
Obj_carro_sedanes.Apagado()
Obj_carro_sedanes.Aceleracion_y_frenado()
Obj_carro_sedanes.Sistema_direccion()
Obj_carro_sedanes.Climatizacion()
Obj_carro_sedanes.Tipo_seguridad()
Obj_carro_sedanes.Luces()
Obj_carro_sedanes.Sistema_ventanas()
Obj_carro_sedanes.Sistema_espejo()


## CARROS SUVs
print("INFORMACION DE LOS CARROS SUVs \n\n")
Obj_carro_SUVs = Carros_SUVs('321 2010\n', 'blanco\n', '15 caballos de fuerza\n', '4 puertas\n', '5 pasajeros\n', 'gasolina\n\n')
Obj_carro_SUVs.Imprimir_datos()
Obj_carro_SUVs.Arranque()
Obj_carro_SUVs.Apagado()
Obj_carro_SUVs.Aceleracion_y_frenado()
Obj_carro_SUVs.Sistema_direccion()
Obj_carro_SUVs.Climatizacion()
Obj_carro_SUVs.Tipo_seguridad()
Obj_carro_SUVs.Luces()
Obj_carro_SUVs.Sistema_ventanas()
Obj_carro_SUVs.Sistema_espejo()


## CARROS COUPES
print("INFORMACION DE LOS CARROS COUPES \n\n")
Obj_carro_sedanes = Carros_coupes('321 2025\n', 'gris\n', '12 caballos de fuerza\n', '2 puertas\n', '5 pasajeros\n', 'diesel\n\n')
Obj_carro_sedanes.Imprimir_datos()
Obj_carro_sedanes.Arranque()
Obj_carro_sedanes.Apagado()
Obj_carro_sedanes.Aceleracion_y_frenado()
Obj_carro_sedanes.Sistema_direccion()
Obj_carro_sedanes.Climatizacion()
Obj_carro_sedanes.Tipo_seguridad()
Obj_carro_sedanes.Luces()
Obj_carro_sedanes.Sistema_ventanas()
Obj_carro_sedanes.Sistema_espejo()






        
        