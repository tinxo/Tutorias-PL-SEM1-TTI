# Código empleado en el tratamiento del tema funciones.

# Definición de la función
def suma(a, b):
    # Devuelve la suma de dos valores que se ingresan como parámetros
    return a + b


# Invocación o llamada a la función
print('Se solicitan dos valores y se realiza la suma')
valorA = int(input('Ingrese el primer valor: '))
valorB = int(input('Ingrese el segundo valor: '))
res = suma(valorA, valorB)
print(f'Resultado de la suma: {res}')
