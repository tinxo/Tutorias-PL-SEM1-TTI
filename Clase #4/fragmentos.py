''' Código usado en la presentación de la clase '''

# Clase de ejemplo para el desarrollo posterior


class Libro:
    ''' Clase Libro (esta es una cadena de descripción) '''

    def __init__(self, titulo, autor, anioPublicacion, cantidadEjemplares,
                 precioUnitario):
        self.titulo = titulo
        self.autor = autor
        self.anioPublicacion = anioPublicacion
        self.cantidadEjemplares = cantidadEjemplares
        self.precioUnitario = precioUnitario

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def getCantidadEjemplares(self):
        return self.cantidadEjemplares

    def __str__(self):
        unLibro = f'{self.titulo} ({self.anioPublicacion}). {self.autor}'
        return unLibro

    def getAntiguedad(self):
        return 2020 - self.anioPublicacion

    def getPrecioVenta(self, pctGanancia):
        return ((pctGanancia / 100) + 1) * self.precioUnitario


# Carga de libros


def cargarLibros():
    print('-' * 50)
    print('Se inicia la carga de libros.')
    libros = []  # Se inicializa una lista vacía
    opcion = True
    while opcion:
        # Se sigue cargando
        tituloTemp = input('Ingrese el título: ')
        autorTemp = input('Ingrese el autor/a: ')
        anioPublicacionTemp = input('Ingrese el año de publicación: ')
        precioUnitarioTemp = float(input('Ingrese el precio unitario: $'))
        cantEjemplaresTemp = int(input('Ingrese la cantidad de ejemplares: '))
        unLibro = Libro(titulo=tituloTemp, autor=autorTemp,
                        anioPublicacion=anioPublicacionTemp,
                        cantidadEjemplares=cantEjemplaresTemp,
                        precioUnitario=precioUnitarioTemp)
        libros.append(unLibro)
        eleccion = input('¿Desea seguir cargando? S/N: ')
        if (eleccion != 'S'):
            opcion = False
    print('Carga de libros finalizada.')
    print('-' * 50)
    return libros  # Se devuelve el resultado de la carga


def imprimirLibros(libros):
    print('-' * 50)
    print('Libros disponibles:')
    id = 0
    for unLibro in libros:
        print(f'#{id} - {unLibro} - Stock: \
{unLibro.getCantidadEjemplares()} unidades.')
        id += 1
    print('-' * 50)


datos = []
datos = cargarLibros()
imprimirLibros(datos)
