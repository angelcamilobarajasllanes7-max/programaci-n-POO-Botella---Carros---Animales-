from CODIGO_GENERAL import Carro
from CARRO_SEDAN import Carros_sedanes
from CARRO_SUVs import Carros_SUVs
from CARRO_COUPES import Carros_coupes


## CODIGO PRINCIPAL

## CARROS SEDANES
print("INFORMACION DE LOS CARROS SEDANES\n\n")
Obj_carro_sedanes = Carros_sedanes('123 2018\n', 'negro\n', '8 caballos de fuerza\n', '4 puertas\n', '5 pasajeros\n', 'gasolina\n\n')
Obj_carro_sedanes.Imprimir_datos()
Obj_carro_sedanes.Arranque()
Obj_carro_sedanes.Apagado()
Obj_carro_sedanes.Aceleracion_y_frenado()
Obj_carro_sedanes.Sistema_direccion()
Obj_carro_sedanes.Climatizacion()
Obj_carro_sedanes.Tipo_seguridad()
Obj_carro_sedanes.Luces()
Obj_carro_sedanes.Sistema_ventanas()
Obj_carro_sedanes.Sistema_espejo()


## CARROS SUVs
print("INFORMACION DE LOS CARROS SUVs \n\n")
Obj_carro_SUVs = Carros_SUVs('321 2010\n', 'blanco\n', '15 caballos de fuerza\n', '4 puertas\n', '5 pasajeros\n', 'gasolina\n\n')
Obj_carro_SUVs.Imprimir_datos()
Obj_carro_SUVs.Arranque()
Obj_carro_SUVs.Apagado()
Obj_carro_SUVs.Aceleracion_y_frenado()
Obj_carro_SUVs.Sistema_direccion()
Obj_carro_SUVs.Climatizacion()
Obj_carro_SUVs.Tipo_seguridad()
Obj_carro_SUVs.Luces()
Obj_carro_SUVs.Sistema_ventanas()
Obj_carro_SUVs.Sistema_espejo()


## CARROS COUPES
print("INFORMACION DE LOS CARROS COUPES \n\n")
Obj_carro_sedanes = Carros_coupes('321 2025\n', 'gris\n', '12 caballos de fuerza\n', '2 puertas\n', '5 pasajeros\n', 'diesel\n\n')
Obj_carro_sedanes.Imprimir_datos()
Obj_carro_sedanes.Arranque()
Obj_carro_sedanes.Apagado()
Obj_carro_sedanes.Aceleracion_y_frenado()
Obj_carro_sedanes.Sistema_direccion()
Obj_carro_sedanes.Climatizacion()
Obj_carro_sedanes.Tipo_seguridad()
Obj_carro_sedanes.Luces()
Obj_carro_sedanes.Sistema_ventanas()
Obj_carro_sedanes.Sistema_espejo()

