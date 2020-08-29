# Declaración de variables

# <nombreVariable> = <valor>

numeroEntero = 101

numeroDecimal = 34.2

valorBoolean = True

texto = 'Texto a guardar'  
# Se pueden usar tanto comillas simples como dobles

# -------------------------

# Tipos de datos: detección y conversiones

# 1ro: Obtener el tipo de datos de una variable -- método type()

print(type(numeroEntero))

# 2do: Cada tipo tiene su método aplicable para conversión

# Pasar a tipo string --> método str()

numeroConvertido = str(numeroEntero)
print(type(numeroConvertido))

# Pasar a tipo entero --> método int()
textoConNumero = '50'
textoConvertido = int(textoConNumero)
print(type(textoConvertido))

# -------------------------

# Operadores de asignación, aritméticos y de comparación

num1 = 5
num2 = 10

# Asignación

res = num1
res += num2
print(f'Qué valor va a tener la variable? {res}')

# Aritméticos

print(f'Suma: {num1 + num2}')
print(f'Resta: {num1 - num2}')
print(f'Multiplicación: {num1 * num2}')
print(f'División: {num1 / num2}')
print(f'Módulo: {num1 % num2}')

# Comparación

print(num1 < num2)  # menor que
print(num1 > num2)  # mayor que
num3 = 5
print(num1 == num3)  # igualdad
print(num1 != num3)  # diferencia
print(num1 <= num3)  # menor o igual
print(num1 >= num3)  # mayor o igual
