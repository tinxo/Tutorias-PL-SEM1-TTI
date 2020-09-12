# Introducción a la POO con python

# Definición de una clase

# class <Nombre>:
#   <componentes de la clase>

class Libro:
    ''' Clase Libro (esta es una cadena de descripción) '''

    # Toda clase tiene que tener un método constructor
    #   Es el método que asigna valores iniciales a los atributos de la clase

    '''
    def __init__(<variables para inicializar atributos>):
        <atributo> = <valor de las variables-parámetros>
    '''

    def __init__(self, titulo, autor, anioPublicacion):
        self.titulo = titulo
        self.autor = autor
        self.anioPublicacion = anioPublicacion
        # self es la forma de indicar un nombre del atributo
        #   cuando se hace referencia a la misma clase

    # Después del método constructor se suelen definir otros
    #   para obtener los valores de los atributos
    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    # Además de los get y los set una clase puede tener otros
    #   métodos para hacer operaciones concretas
    def __str__(self):
        # En este caso el método sirve para obtener el objeto
        #   transformado a un tipo string
        unLibro = f'{self.titulo} ({self.anioPublicacion}). {self.autor}'
        return unLibro

    def getAntiguedad(self):
        # TODO: Cambiar literal 2020 por fecha concreta
        return 2020 - self.anioPublicacion


# Instanciar un objeto
libro1 = Libro('La Sirena', 'Florencia Etcheves', 2019)
print(f'Conversión a string del objeto: {libro1}')
print(f'Título: {libro1.getTitulo()}')
print(f'Resultado de la antiguedad: {libro1.getAntiguedad()}')
