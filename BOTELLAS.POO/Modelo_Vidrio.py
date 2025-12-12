from Modelo_Botella import Botella

class Botella_vidrio(Botella):
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        super().__init__(material, capacidad, forma, diseño, tapa, grabados)
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa
        self.grabados = grabados
        
        
    def Imprimir_datos(self):
        print(f'material: {self.material}')
        print(f'capaciudad: {self.capacidad}')
        print(f'forma: {self.forma}')
        print(f'diseño: {self.diseño}')
        print(f'tapa: {self.tapa}')
        print(f'grabados: {self.grabados}')
        
    def Contener_liquidos(self):
        print("las botellas contienen cerveza\n")

    def Facilitar_vertido(self):
        print("la forma de la botella facilita el vertido del liquido\n")

    def Cierre_hermetico(self):
        print("cierre de la tapa hacia la botella, aplicando temperatura(calor)\n")
    
    def Transporte_botellas(self):
        print("movilizacion de botellas por medio de vehiculos\n")
    
    def Manejar_botellas(self):
        print("manejarlas con el mejor cuidado\n")
    
    def Compatibilidad_bebidas_calientes_frias(self):
        print("puede soportar liquidos calientes o frios\n")

    def Reutilizacion_envase(self):
        print("la botella es retornable\n")
    
    def Transparencia_botella(self):
        print("por lo general las botellas se puede lograr ver el interior del liquido\n")



