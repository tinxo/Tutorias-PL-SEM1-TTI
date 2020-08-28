# Comunicación con el usuario

# Para "imprimir" valores a la consola o intérprete

# Para los casos en los que solo es un texto
print('Texto a imprimir')

valor = 101
# Para los casos en los que además del texto se tiene que imprimir una variable
print(f'Texto y un valor desde una variable, ejemplo: {valor}')
# Las f-strings se usan para no tener que hacer conversiones explícitas de un
#   valor a string para imprimirse

# -----------------------------------

# Para solicitar al usuario el ingreso de un valor

# Método --> input()
# Debe "recibir" el contenido en una variable

edad = input('Ingrese su edad: ')

# Se tiene que considerar que se ingresa como string
