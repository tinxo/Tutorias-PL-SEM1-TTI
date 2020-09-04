# Código empleado en la revisión de las estructuras
# de datos de tipo: tuplas, diccionarios y conjuntos.


# Uso de tuplas

unaTupla = ('uno', 2, 'tres', 4.0)

#print(f'El segundo elemento es: {unaTupla[1]}')

#unaTupla[0] = 'cero'  # Genera un TypeError

# -----------------------------------------

# Uso de diccionarios

unDiccionario = {'a': 'arbol', 2: 'barco', 'c': 'carta'}

print(unDiccionario[2])

# Método --> keys() obtiene todas las claves
print(f'Claves del diccionario {unDiccionario.keys()}')

# Método --> items() devuelve todo el contenido
print(f'Todo el diccionario: {unDiccionario.items()}')

# Agregado de un elemento más
unDiccionario[4] = 'dado'

# Recorrido de un diccionario

for clave in unDiccionario.keys():
    print(f'La clave {clave} tiene el valor {unDiccionario[clave]}')

# -----------------------------------------

# Uso de sets

unSet = {6, 0}
print(unSet[0])  # Genera un TypeError

# Forma válida para inicializar
nuevoSet = set()
print(nuevoSet)

# Método --> add() para agregar un elemento
unSet.add(7)
print(unSet)

# Método --> remove() para eliminar un elemento
unSet.remove(0)
print(unSet)
# Si no existe el elemento remove() genera un error
