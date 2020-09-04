# Ordenación de valores
# Método --> sort()

marcas = ['Alfa Romeo', 'Maseratti', 'Ferrari', 'Lancia']

marcas.sort()
print(f'Orden ascendente: {marcas}')

marcas.sort(reverse=True)
print(f'Orden descendente: {marcas}')


def cantidadCaracteres(valor):
    return len(valor)


marcas.sort(key=cantidadCaracteres)
print(f'Orden por cantidad de letras en nombre: {marcas}')

# ---------------------------------

# Búsqueda de valores

lenguajes = ['python', 'c', 'java', 'php', 'sql']


# Buscar si un valor existe dentro de una lista
def buscar(lista, valorBuscado):
    encontrado = False
    for elemento in lista:
        if (elemento == valorBuscado):
            encontrado = True
            break
    return encontrado


if (buscar(lenguajes, 'pascal')):
    print('Se encontró el dato buscado.')
else:
    print('No se encontró el dato buscado.')

# También hay métodos para búsqueda

# Operador --> in para saber si un elemento está en una lista
# Método --> index() devuelve el índice de un valor

if ('java' in lenguajes):
    print(f'La posición de java es: {lenguajes.index("java")}')

# ---------------------------------

# Búsqueda de mayor / menor

valores = [20, 3, 5, -1, 25, 6]


def obtenerMayor(lista):
    mayor = lista[0]
    for num in lista:
        if (num > mayor):
            mayor = num
    return mayor


print(f'La lista de valores: {valores}')
print(f'El valor más alto de la lista es: {obtenerMayor(valores)}')
