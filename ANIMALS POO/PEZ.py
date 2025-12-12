from MODELO_ANIMAL import Animal

class Pez(Animal):
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
        print("movimientos del cuerpo y la cola, y el uso de las aletas para dirigir, estabilizar y maniobrar")

    def Comunicacion(self):
        print("vibraciones, que incluyen bramidos, gruñidos, toses y siseos")

    def Reproduccion(self):
        print("Los peces se reproducen principalmente por fecundación externa ovípara (ponen huevos que son fecundados fuera del cuerpo)")

    def Alimentarse(self):
        print("Los peces se alimentan de diversas formas según su especie y hábitat, clasificándose como carnívoros, herbívoros, omnívoros o filtradores")

    def Adaptacion(self):
        print("Los peces se adaptan a su entorno acuático a través de adaptaciones como las branquias para respirar bajo el agua,")

    def Instintos(self):
        print("Los instintos de los peces incluyen la alimentación, migración, reproducción (como el cortejo y la construcción de nidos)")

    def Descanso(self):
        print("El descanso de los peces consiste en reducir drásticamente su actividad física y metabólica")

    def Sueño(self):
        print("Los peces duermen con los ojos abiertos, ya que carecen de párpados")

    def Interaccion_social(self):
        print("s incluye comportamientos como la formación de bancos, la competencia por recursos, el cortejo y el apareamiento, y la comunicación")


