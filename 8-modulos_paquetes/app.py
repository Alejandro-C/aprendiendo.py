import modulo  # importar un módulo que no pertenece a un paquete
import paquete.modulo1  # importar un módulo que está dentro de un paquete
import paquete.modulo2 as modulo2
import paquete.subpaquete.submodulo1 as submodulo  # importar un módulo que está dentro de un subpaquete

print(modulo.mensaje)
print(paquete.modulo1.mensaje)
print(modulo2.mensaje)
print(submodulo.mensaje)