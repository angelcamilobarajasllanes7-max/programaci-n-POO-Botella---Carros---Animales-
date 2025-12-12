
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





## CODIGO PRINCIPAL ##

## CLASE CABALLO ##

print("INFORMACION DEL ANIMAL CABALLO")

Obj_caballo = Caballo('caballo\n', 'de 25 a 30 años', ' llanuras y zonas semidesérticas', 'se alimentan de forraje', '1.47 metros (14.2 manos) a 1.68 metros a la cruz', 'castaño, negro y alazán (un castaño rojizo)')
Obj_caballo.Moverse()
Obj_caballo.Comunicacion()
Obj_caballo.Reproduccion()
Obj_caballo.Alimentarse()
Obj_caballo.Adaptacion()
Obj_caballo.Instintos()
Obj_caballo.Descanso()
Obj_caballo.Sueño()
Obj_caballo.Interaccion_social()



## CLASE CAIMAN ##

print("INFORMACION DEL ANIMAL CAIMAN")

Obj_caiman = Caiman('caiman\n', '30 y 75 años', 'aguas dulces como pantanos, ciénagas, estanques, lagos', ' compuesta por peces, aves, reptiles, anfibios y mamíferos pequeños y grandes', 'promedio entre \(1.5\) y \(3\) metros', ' gris oscuro, marrón, negro o verde oliva mate')
Obj_caiman.Moverse()
Obj_caiman.Comunicacion()
Obj_caiman.Reproduccion()
Obj_caiman.Alimentarse()
Obj_caiman.Adaptacion()
Obj_caiman.Instintos()
Obj_caiman.Descanso()
Obj_caiman.Sueño()
Obj_caiman.Interaccion_social()



## CLASE PEZ

print("INFORMACION DEL ANIMAL PEZ")

Obj_pez = Pez('pez\n', ' un promedio general es de tres a cinco años', 'aguas dulces o agua salada', ' lagas, fotoplanton, zooplanton', 'promedio entre 6 – 8 cm', ' de todos los colores')
Obj_pez.Moverse()
Obj_pez.Comunicacion()
Obj_pez.Reproduccion()
Obj_pez.Alimentarse()
Obj_pez.Adaptacion()
Obj_pez.Instintos()
Obj_pez.Descanso()
Obj_pez.Sueño()
Obj_pez.Interaccion_social()


## CLASE ESCARABAJO ##

print("INFORMACION DEL ANIMAL ESCARABAJO")

Obj_escarabajo = Escarabajo('escarabajo\n', 'unas pocas semanas a varios años', 'habitan en casi todos los ecosistemas terrestres y acuáticos, excepto en las regiones polares extremas', 'hojas, tallos, frutos, néctar, madera', 'entre 4 - 6cm', ' de todos los colores')
Obj_escarabajo.Moverse()
Obj_escarabajo.Comunicacion()
Obj_escarabajo.Reproduccion()
Obj_escarabajo.Alimentarse()
Obj_escarabajo.Adaptacion()
Obj_escarabajo.Instintos()
Obj_escarabajo.Descanso()
Obj_escarabajo.Sueño()
Obj_escarabajo.Interaccion_social()


## CLASE PATO ##

print("INFORMACION DEL ANIMAL PATO")

Obj_pato = Pato('pato\n', ' de 8 a 12 años', 'areas húmedas con agua dulce como lagos, estanquess', 'plantas, semillas, insectos, gusanos y pequeños crustáceos', 'entre 50 – 65 cm', ' de todos los colores')
Obj_pato.Moverse()
Obj_pato.Comunicacion()
Obj_pato.Reproduccion()
Obj_pato.Alimentarse()
Obj_pato.Adaptacion()
Obj_pato.Instintos()
Obj_pato.Descanso()
Obj_pato.Sueño()
Obj_pato.Interaccion_social()




    

    
        