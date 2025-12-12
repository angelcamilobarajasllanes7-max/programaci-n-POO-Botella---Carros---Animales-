class Animal():
    def __init__(self, nombre, edad , habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    def Imprimir_datos(self):
        print(f'nombre del animal: {self.nombre}')
        print(f'edad: {self.edad}')
        print(f'habitat: {self.habitat}')
        print(f'dieta: {self.dieta}')
        print(f'tamaño: {self.tamaño}')
        print(f'color: {self.color}')

    def Moverse(self):
        print("se mueve para todos lados")

    def Comunicacion(self):
        print("cada especie se comunica de una forma distinta")

    def Reproduccion(self):
        print("se reproducen sexualmente")

    def Alimentarse(self):
        print("cada animal tiene una alimentacion distinta")

    def Adaptacion(self):
        print("hay animales que soportan climas extremos pero hay otros que son todo lo contrario")

    def Instintos(self):
        print("los siempre destacan por tener sentidosmuy agudos, mas aun cuando so depredadores")

    def Descanso(self):
        print("por ,o general duermen de noche")

    def Sueño(self):
        print("dependiendo de la especie, ya que unas toman sistas, ya que no se puede descuidar mucho en el reino animal")

    def Interaccion_social(self):
        print("por lo general hay conflictos en animales de la misma especie")

