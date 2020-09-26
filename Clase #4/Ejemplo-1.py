''' Código usado en la presentación de la clase '''

# Clase de ejemplo para el desarrollo posterior


class Libro:
    ''' Clase Libro (esta es una cadena de descripción) '''

    def __init__(self, titulo, autor, anioPublicacion, cantidadEjemplares,
                 precioUnitario):
        self.titulo = titulo
        self.autor = autor
        self.anioPublicacion = anioPublicacion

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def __str__(self):
        unLibro = f'{self.titulo} ({self.anioPublicacion}). {self.autor}'
        return unLibro

    def getAntiguedad(self):
        return 2020 - self.anioPublicacion


# Carga de libros


def cargarLibros():
    libros = []  # Se inicializa una lista vacía
    opcion = True
    while opcion:
        # Se sigue cargando
        tituloTemp = input('Ingrese el título: ')
        autorTemp = input('Ingrese el autor/a: ')
        anioPublicacionTemp = input('Ingrese el año de publicación: ')
        unLibro = Libro(titulo=tituloTemp, autor=autorTemp,
                        anioPublicacion=anioPublicacionTemp)
        libros.append(unLibro)
        eleccion = input('¿Desea seguir cargando? S/N: ')
        if (eleccion != 'S'):
            opcion = False
    return libros  # Se devuelve el resultado de la carga


def imprimirLibros(libros):
    id = 0
    for unLibro in libros:
        print(f'#{id} - {unLibro}')
        id += 1


def seleccionarLibro(operacion, libros):
    imprimirLibros(libros)
    if (operacion == 'U'):
        idLibro = int(input('Ingrese el número del libro a modificar: '))
        unLibro = libros[idLibro]
        libros[idLibro] = modificarLibro(unLibro)
    else:
        idLibro = int(input('Ingrese el número del libro a eliminar: '))
        libros = eliminarLibro(libros, idLibro)
    return libros


def modificarLibro(modificable):
    print('Inicia actualización de datos:')
    tituloTemp = input('Ingrese el nuevo título: ')
    autorTemp = input('Ingrese los datos del nuevo autor/a: ')
    anioPublicacionTemp = input('Ingrese el nuevo año de publicación: ')
    unLibro = Libro(titulo=tituloTemp, autor=autorTemp,
                    anioPublicacion=anioPublicacionTemp)
    return unLibro


def eliminarLibro(libros, eliminable):
    print('Confirma que desea eliminar el siguiente libro?')
    unLibro = libros[eliminable]
    print(f'{unLibro}')
    confirmar = input('Confirma eliminación? S / N ')
    if (confirmar == 'S'):
        libros.remove(unLibro)
    return libros


def menu():
    datos = []
    print('Inicio - CRUD básico')
    opcion = 'P'
    while (opcion != 'X'):
        print('Seleccione la opción a ejecutar:')
        print('[C] Agregar libros')
        print('[R] Obtener listado de libros')
        print('[U] Modificar un libro')
        print('[D] Eliminar un libro')
        print('[X] Salir')
        opcion = input('Opción elegida: ')
        if (opcion == 'C'):
            datos = cargarLibros()
        elif (opcion == 'R'):
            imprimirLibros(datos)
        elif (opcion == 'U' or opcion == 'D'):
            datos = seleccionarLibro(opcion, datos)


menu()
