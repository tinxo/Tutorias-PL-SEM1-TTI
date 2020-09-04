# Búsqueda y búsqueda ordenada - Ejemplo para el Tema 3

# Buscar si un valor existe dentro de una lista
def buscar(lista, valorBuscado):
    encontrado = False
    for elemento in lista:
        if (elemento == valorBuscado):
            encontrado = True
            break
    return encontrado

def busquedaOrdenada(lista, valorBuscado):
    lista.sort()
    encontrado = False
    for elemento in lista:
        print(elemento)
        if (elemento == valorBuscado):
            encontrado = True
            break
        elif (elemento > valorBuscado):
            break
    return encontrado


lenguajes = ['python', 'c', 'java', 'php', 'sql']
valores = [18, 5, 9, 3, -2, 10]
if (busquedaOrdenada(valores, 4)):
    print('Se encontró el dato buscado.')
else:
    print('No se encontró el dato buscado.')
