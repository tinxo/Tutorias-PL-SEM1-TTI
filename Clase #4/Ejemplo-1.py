''' Código usado en la presentación de la clase '''

# Clase de ejemplo para el desarrollo posterior


class Libro:
    ''' Clase Libro (esta es una cadena de descripción) '''

    def __init__(self, titulo, autor, anioPublicacion, cantidadEjemplares, precioUnitario):
        self.titulo = titulo
        self.autor = autor
        self.anioPublicacion = anioPublicacion
        # Agregados
        self.cantidadEjemplares = cantidadEjemplares
        self.precioUnitario = precioUnitario

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def __str__(self):
        unLibro = f'{self.titulo} ({self.anioPublicacion}). {self.autor}'
        return unLibro

    def getAntiguedad(self):
        return 2020 - self.anioPublicacion

    # Agregados en ejemplo
    def getCantidadEjemplares(self):
        return self.cantidadEjemplares

    def getPrecioVenta(self, pctGanancia):
        # ((% / 100) + 1) * precioUnitario >>
        #           (35 / 100) + 1 = 1.35 * precioUnitario
        return ((pctGanancia / 100) + 1) * self.precioUnitario

# Carga de libros


def cargarLibros():
    libros = []  # Se inicializa una lista vacía
    opcion = True
    while opcion:
        print('-' * 50)
        # Se sigue cargando
        tituloTemp = input('Ingrese el título: ')
        autorTemp = input('Ingrese el autor/a: ')
        anioPublicacionTemp = input('Ingrese el año de publicación: ')
        precioTemp = float(input('Ingrese el precio unitario: $ '))
        cantEjemplaresTemp = int(input('Ingrese la cantidad de ejemplares: '))
        unLibro = Libro(titulo=tituloTemp, autor=autorTemp,
                        anioPublicacion=anioPublicacionTemp,
                        cantidadEjemplares=cantEjemplaresTemp,
                        precioUnitario=precioTemp)
        libros.append(unLibro)
        eleccion = input('¿Desea seguir cargando? S/N: ')
        if (eleccion != 'S'):
            opcion = False
    return libros  # Se devuelve el resultado de la carga


def imprimirLibros(libros):
    print('-' * 50)
    id = 0
    for unLibro in libros:
        print(f'#{id} - {unLibro} - Stock: {unLibro.getCantidadEjemplares()} unidades')
        id += 1


def seleccionarLibro(operacion, libros):
    imprimirLibros(libros)
    print('-' * 50)
    if (operacion == 'U'):
        idLibro = int(input('Ingrese el número del libro a modificar: '))
        libros = modificarLibro(libros, idLibro)
    else:
        idLibro = int(input('Ingrese el número del libro a eliminar: '))
        libros = eliminarLibro(libros, idLibro)
    return libros


def modificarLibro(libros, modificable):
    print('-' * 50)
    print('Inicia actualización de datos:')
    temp = libros[modificable]
    tituloTemp = input(f'Ingrese el nuevo título para {temp.getTitulo()}: ')
    autorTemp = input(f'Ingrese los datos del nuevo autor/a: ')
    anioPublicacionTemp = input('Ingrese el nuevo año de publicación: ')
    precioTemp = float(input('Ingrese el nuevo precio unitario: $ '))
    cantEjemplaresTemp = int(input('Ingrese la nueva cantidad de ejemplares: '))
    unLibro = Libro(titulo=tituloTemp, autor=autorTemp,
                        anioPublicacion=anioPublicacionTemp,
                        cantidadEjemplares=cantEjemplaresTemp,
                        precioUnitario=precioTemp)
    libros[modificable] = unLibro
    return libros


def eliminarLibro(libros, eliminable):
    print('-' * 50)
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
        print('-' * 50)
        print('Seleccione la opción a ejecutar:')
        print('[C] Agregar libros')
        print('[R] Obtener listado de libros')
        print('[U] Modificar un libro')
        print('[D] Eliminar un libro')
        print('[G] Calcular ingresos x venta de todo el stock')
        print('[X] Salir')
        opcion = input('Opción elegida: ')
        if (opcion == 'C'):
            datos = cargarLibros()
        elif (opcion == 'R'):
            imprimirLibros(datos)
        elif (opcion == 'U' or opcion == 'D'):
            datos = seleccionarLibro(opcion, datos)
        elif (opcion == 'G'):
            calcularGanaciasVenta(datos)

# Consigna: se desea saber qué ganancias se pueden obtener 
# vendiendo todos los libros
# con un margen de utilidad del 25%


def calcularGanaciasVenta(datos):
    print('-' * 50)
    utilidadEsperada = 25  # 25%
    total = 0
    for unLibro in datos:
        precioVenta = unLibro.getPrecioVenta(utilidadEsperada)
        montoVentas = precioVenta * unLibro.getCantidadEjemplares()
        total += montoVentas
    print(f'Vendiendo todo el stock de libros se pueden obtener ingresos por ${total}')


menu()
