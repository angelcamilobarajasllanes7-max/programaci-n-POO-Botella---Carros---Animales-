from MODELO_ANIMAL import Animal

class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
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
        print("se mueve en galopa")

    def Comunicacion(self):
        print("a través de una combinación de lenguaje corporal, vocalizaciones, lenguaje táctil y olfativo")

    def Reproduccion(self):
        print("Los caballos se reproducen sexualmente y de manera vivípara")

    def Alimentarse(self):
        print(" principalmente de forraje (hierba, heno, paja), complementando su dieta con pienso concentrado, frutas y verduras en moderación, y sal")

    def Adaptacion(self):
        print("pelaje que se vuelve más denso en invierno, y cascos duros para moverse en superficies variadas")

    def Instintos(self):
        print(" la huida (debido a ser un animal de presa) y el gregario (vivir en grupo)")

    def Descanso(self):
        print("tienen un sueño ligero de pie.  Su sistema de bloqueo en las patas les ayuda a descansar sin caerse.")

    def Sueño(self):
        print("Los caballos duermen tanto de pie como acostados, pero para lograr un sueño profundo (fase REM) deben recostarsel")

    def Interaccion_social(self):
        print("las interacciones se manifiestan a través de la comunicación visual, sonora y el contacto físico, como el acicalamiento mutuo")

