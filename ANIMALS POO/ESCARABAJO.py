from MODELO_ANIMAL import Animal

class Escarabajo(Animal):
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
        print("nada en el agua y se mueve usando sus patas traseras adaptadas como remos")

    def Comunicacion(self):
        print("principalmente a través de feromonas (señales químicas) y señales táctiles (contacto físico), aunque otras especies también usan sonidos y vibraciones")

    def Reproduccion(self):
        print("se reproducen sexualmente: el macho y la hembra se aparean y, después, la hembra deposita los huevos en la vegetación acuática, el barro o la madera cerca del agua")

    def Alimentarse(self):
        print("se alimentan de una dieta variada que incluye excrementos, carroña, materia vegetal en descomposición, plantas vivas, hongos y otros insectos.")

    def Adaptacion(self):
        print("a través de su exoesqueleto resistente, sus élitros protectores y un par de alas para el vuelo")

    def Instintos(self):
        print(" la orientación por el cielo (sol, luna, Vía Láctea) para navegar")

    def Descanso(self):
        print(" ocurre en lugares seguros como nidos, agujeros en el suelo, o entre la vegetación")

    def Sueño(self):
        print(" ocurre en lugares seguros como nidos, agujeros en el suelo, o entre la vegetación")

    def Interaccion_social(self):
        print("la mayoría son solitarios")


