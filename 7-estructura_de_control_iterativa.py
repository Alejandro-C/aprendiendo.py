''' Bucle While '''
# Mientras que año sea menor o igual a 2012, imprimir la frase “Informes del Año año”

anio = 2001

while anio <= 2010:
    print('informes de año', anio)
    anio += 1


''' Bucle For '''
# Por cada nombre en miLista, imprimir nombre

miLista = ['Ever', 'Alejandro', 'Dimar', 'Yoney', 'Jusus']

for nombre in miLista:
    print(nombre)

# Por cada año en el rango 2001 a 2013, imprimir la frase “Informes del Año año”

for anio in range(2001, 2010):
    print('informes de año', anio)