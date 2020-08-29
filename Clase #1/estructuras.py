# Estructura IF (selectiva)

# Sirve para que el programa realice una serie de acciones en
# función de una condición

nota = 7
if (nota >= 6):
    # Se definen las acciones a ejecutar si la condición = VERDADERO (True)
    print('Aprobado')

# Para el caso en el que tenga que controlar lo que pasa ante una
#   condición FALSA (False) se usa el bloque Else
asistencia = 76
if (nota >= 6) and (asistencia >= 75):
    print('Regular')
else:
    print('Libre')

# Para las condiciones moleculares se usan los conectores lógicos

''' Esto es un comentario multi-línea

and     -->     conector lógico Y (conjunción)
or      -->     conector lógico O (disyunción)
not     -->     operador de negación

'''

# -------------------------------------------------

# Estructura FOR (repetitiva)

# Sirve para repetir una serie de instrucciones por un número de ocasiones

# Se puede usar con una variable auxiliar que toma valores dentro de un rango
#   de manera tal que "recorra" desde un valor hasta un límite
for i in range(5):
    # En este caso se va a repetir la acción de imprimir el valor de i
    print(i)

# El método range(<valor>) genera un listado de números entre 0 y el
#   valor ingresado (no lo incluye). Ver las otras opciones.

# -------------------------------------------------

# Estructura VHILE (iterativa)

# Sirve para repetir una serie de instrucciones mientras una
#   condición sea VERDADERA (True)

valorInicial = 10
while (valorInicial > 0):
    print(f'Restan {valorInicial} iteraciones.')
    valorInicial -= 1

print(f'La variable finalizó con valor: {valorInicial}')
