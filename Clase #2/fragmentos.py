# Código empleado en la introducción estructuras de datos

# Caso de inicio - Clientes y saldos de cuenta

cliente1 = 200.50
cliente2 = 2542.00
cliente3 = 539.21

# --------------------------------------------

# Definición de una lista
# <nombre-variable> = [<elemento>, <elemento>]

clientes = [200.50, 2542.00, 539.21]

mascotas = ['Leo', 'Lana', 'Milo']

mixto = [15, '20', 'datos', 3.75, True]
# Pueden tener datos heterogéneos

# --------------------------------------------

# Para acceder a un elemento se usa el nombre
#   de la variable y entre corchetes la posición
#   a la que se desea acceder

precios = [79.6, 104.54, 138.9]

print(f'Valor en la posición 1 = {precios[1]}')
pos = 0  # Se tiene que usar un número entero
print(f'Valor en la posición {pos} = {precios[pos]}')

# Para modificar un valor se puede hacer una asignación
precios[2 - 2] = 78.75
print(precios)


# Para agregar un elemento

# Método --> append() agrega al final
original = ['A', 'B', 'C']
original.append('F')
print(f'Lista modificada: {original}')

# Método --> insert() para agregar en una posición

original.insert(3, 'D')
print(f'Lista modificada: {original}')


# Lectura de los valores desde el teclado
notas = []
print('Se van a cargar las notas de cinco alumnos.')
for i in range(5):
    valor = float(input(f'Ingrese la {i+1}° nota: '))
    notas.append(valor)

# Se puede usar un bucle for para iterar sobre la lista
promedio = 0
for nota in notas:
    promedio += nota
print(f'Promedio de notas = {promedio / len(notas)}')
