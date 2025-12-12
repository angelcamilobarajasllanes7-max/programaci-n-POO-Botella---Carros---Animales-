class Botella():
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
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
        contenido_botellas = "las botellas contienen agua"
        return contenido_botellas

    def Facilitar_vertido(self):
        vertido = "la forma de la botella facilita el vertido del liquido"
        return vertido

    def Cierre_hermetico(self):
        cierre_tapa = "cierre de la tapa hacia la botella, aplicando temperatura(calor)"
        return cierre_tapa
    
    def Transporte_botellas(self):
        transporte = "movilizacion de botellas por medio de vehiculos"
        return transporte
    
    def Manejar_botellas(self):
        manejar = "en lo posible manejarlas con el mejor cuidado"
        return manejar
    
    def Compatibilidad_bebidas_calientes_frias(self):
        compatibilidad = "no se llevan muy bien que digamos"
        return compatibilidad

    def Reutilizacion_envase(self):
        envase = "la botella se puede reutilizar de muchas formas sea plastica o de vidrio"
        return envase
    
    def Transparencia_botella(self):
        transparencia = "por lo general las botellas se puede lograr ver el interior del liquido"     
        return transparencia
    
    

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



class Botella_plastica(Botella):
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
        print("las botellas contienen malta\n")

    def Facilitar_vertido(self):
        print("la forma de la botella facilita el vertido del liquido\n")

    def Cierre_hermetico(self):
        print("cierre de la tapa hacia la botella, aplicando temperatura(calor)\n")
    
    def Transporte_botellas(self):
        print("movilizacion de botellas por medio de vehiculos\n")
    
    def Manejar_botellas(self):
        print("manejarlas con el mejor cuidado\n")
    
    def Compatibilidad_bebidas_calientes_frias(self):
        print("puede soportar liquidos liquidos frios pero no que esten muy calientes\n")

    def Reutilizacion_envase(self):
        print("la botella no es tan retornable\n")
    
    def Transparencia_botella(self):
        print("por lo general las botellas se puede lograr ver el interior del liquido\n\n")


        
        
##CODIGO PRINCIPAL##     

## BOTELLA DE VIDRIO 


print("INFORMACION BOTELLAS DE VIDRIO \n\n")

Obj_Botella_vidrio = Botella_vidrio('vidrio \n', '400ml\n', 'rectangular\n','vidrio oscuro\n', 'de metal\n', 'coca-cola\n\n')
Obj_Botella_vidrio.Imprimir_datos()
Obj_Botella_vidrio.Contener_liquidos()
Obj_Botella_vidrio.Facilitar_vertido()
Obj_Botella_vidrio.Cierre_hermetico()
Obj_Botella_vidrio.Transporte_botellas()
Obj_Botella_vidrio.Manejar_botellas()
Obj_Botella_vidrio.Compatibilidad_bebidas_calientes_frias()
Obj_Botella_vidrio.Reutilizacion_envase()
Obj_Botella_vidrio.Transparencia_botella()


## BOTELLA PLASTICA

print("INFROMACION BOTELLA PLASTICA\n\n")
Obj_Botella_plastica = Botella_plastica('plastico \n', '400ml\n', 'perpendicular\n','plastico trasparente\n', 'pastica\n', 'PONY MALTA\n\n')
Obj_Botella_plastica.Imprimir_datos()
Obj_Botella_plastica.Contener_liquidos()
Obj_Botella_plastica.Facilitar_vertido()
Obj_Botella_plastica.Cierre_hermetico()
Obj_Botella_plastica.Transporte_botellas()
Obj_Botella_plastica.Manejar_botellas()
Obj_Botella_plastica.Compatibilidad_bebidas_calientes_frias()
Obj_Botella_plastica.Reutilizacion_envase()
Obj_Botella_plastica.Transparencia_botella()
