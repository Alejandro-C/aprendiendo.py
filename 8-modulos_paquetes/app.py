import modulo  # importar un módulo que no pertenece a un paquete
import paquete.modulo1  # importar un módulo que está dentro de un paquete
import paquete.modulo2
import paquete.subpaquete.submodulo1  # importar un módulo que está dentro de un subpaquete

print(modulo.mensaje)
print(paquete.modulo1.mensaje)
print(paquete.modulo2.mensaje)
print(paquete.subpaquete.submodulo1.mensaje)

# IMPORTAR MODULOS SIN USAR NAMESPACE
# la palabra reservada 'as' es para darle un alias al modulo al que se esta importando
from modulo import mensaje as mensaje1
from paquete.modulo1 import mensaje as mensaje2
from paquete.subpaquete.submodulo1 import mensaje as mensaje3

print('-------------------------')
print(mensaje1)
print(mensaje2)
print(mensaje3)