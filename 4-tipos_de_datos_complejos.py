# TUPLAS
miTupla = (1, 'a', 3, 'e', 5, 'i', 7, 'o', 9, 'u')
print(miTupla)
# Un elemento de la tupla
print(miTupla[2])
# Una seccion de la tupla
print(miTupla[2:6])
# Otra forma de acceder a los elemtosde la tupla
print(miTupla[-1])

# LISTAS
miLista = [1, 'a', 3, 'e', 5, 'i', 7, 'o', 9, 'u']
print(miLista)
# Un elemento de la Lista
print(miLista[2])
# Una seccion de la Lista
print(miLista[2:6])
# Otra forma de acceder a los elemtosde la Lista
print(miLista[-1])
# modificar el valor de una posicion
miLista[1] = 'A'
print(miLista)
# Agregar un nuevo valor a la lista
miLista.append(0)
print(miLista)

# DICCIONARIOS
miDiccionario = { 
    'clave1' : 'valor1', 
    'clave2' : 'valor2', 
    'clave3' : 'valor3'
}
print(miDiccionario)
# acceder a un valor
print(miDiccionario['clave2'])
# eliminar un valor
del(miDiccionario['clave2'])
print(miDiccionario)
# modificar un valor
miDiccionario['clave1'] = 1
print(miDiccionario)