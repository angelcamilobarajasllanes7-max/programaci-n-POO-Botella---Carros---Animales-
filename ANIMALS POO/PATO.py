from MODELO_ANIMAL import Animal

class Pato(Animal):
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
        print("El pato se desplaza volando, nadando y caminando")

    def Comunicacion(self):
        print(" se comunican a través de una variedad de sonidos vocales como graznidos, silbidos, gruñidos y cuacs")

    def Reproduccion(self):
        print("Los patos se reproducen de forma sexual, y la hembra pone huevos que incubará hasta que nazcan los patitos")

    def Alimentarse(self):
        print("Los patos comen una dieta omnívora que incluye plantas, semillas, insectos, gusanos y pequeños crustáceos")

    def Adaptacion(self):
        print("Los patos se adaptan principalmente a través de sus características físicas y comportamentales")

    def Instintos(self):
        print("Los instintos de los patos incluyen el instinto de agrupación para la seguridad, la impronta para seguir al primer ser que ven al nacer")

    def Descanso(self):
        print("El descanso del pato se refiere a su capacidad para dormir con un ojo abierto y la otra mitad del cerebro despierta")

    def Sueño(self):
        print(" sobre una pata para conservar el calor y reducir la fatiga")

    def Interaccion_social(self):
        print("Los patos son animales muy sociales que buscan la compañía de otros de su especie y de los humanos")
