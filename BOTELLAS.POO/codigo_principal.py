from Botella_vidrio import Botella_vidrio 
from Botella_plastica import Botella_plastica
       
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
