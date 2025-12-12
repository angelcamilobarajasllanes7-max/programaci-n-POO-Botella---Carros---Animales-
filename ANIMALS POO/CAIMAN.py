from MODELO_ANIMAL import Animal

class Caiman(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def Imprimir_datos(self):
        print(f'nombre del animal: {self.nombre}')
        print(f'edad: {self.edad}')
        print(f'habitat: {self.habitat}')
        print(f'dieta: {self.dieta}')
        print(f'tamaño: {self.tamaño}')
        print(f'color: {self.color}')

    def Moverse(self):
        print("en el agua usan su poderosa cola para impulsarse  ")

    def Comunicacion(self):
        print("vibraciones, que incluyen bramidos, gruñidos, toses y siseos")

    def Reproduccion(self):
        print("se reproducen durante la temporada de lluvias, con el apareamiento que ocurre bajo el agua")

    def Alimentarse(self):
        print("Los caimanes son carnívoros y su dieta varía con su edad")

    def Adaptacion(self):
        print("a través de adaptaciones físicas y de comportamiento")

    def Instintos(self):
        print("la caza sigilosa mediante camuflaje y emboscadas")

    def Descanso(self):
        print("en diferentes lugares, como el agua poco profunda, bancos de lodo o madrigueras")

    def Sueño(self):
        print("omando el sol o descansando en aguas poco profundas o madrigueras en el lodol")

    def Interaccion_social(self):
        print("generalmente solitaria")


