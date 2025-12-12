
class Base_dato():
    def __init__(self):
        self.lista_modelo_botella = []
        self.lista_modelo_botella_vidrio = []
        self.lista_botella_plastica = []
    
    def agregar_botella(self, botella_nueva):
        self.lista_modelo_botella.append(botella_nueva)
        print(self.lista_modelo_botella)
        
        
    def agregar_botella_vidrio(self, nueva_botella_vidrio):
        self.lista_modelo_botella_vidrio.append(nueva_botella_vidrio)
        print(self.lista_modelo_botella_vidrio)
        
        
    def agregar_botella_plastica(self, nueva_botella_plastica):
        self.lista_botella_plastica.append(nueva_botella_plastica)
        print(self.lista_botella_plastica)
    
        
 
## menu 2- agregar elementos de una lista a otra ##


    def agregar_lista_botella_con_lista_botella_vidrio(self):
        self.lista_modelo_botella.extend(self.lista_botella_plastica)
        print(self.lista_modelo_botella)

    def agregar_lista_botella_con_lista_botella_plastica(self):
        self.lista_modelo_botella.extend(self.lista_botella_plastica)
        print(self.lista_modelo_botella)
        
    def agregar_lista_botella_vidrio_con_lista_botella_plastica(self):
        self.lista_modelo_botella_vidrio.extend(self.lista_botella_plastica)
        print(self.lista_modelo_botella_vidrio)

    def agregar_lista_botella_plastica_con_lista_botella_vidrio(self):
        self.lista_botella_plastica.extend(self.lista_modelo_botella_vidrio)
        print(self.lista_botella_plastica)



## MENU 3- 

    
