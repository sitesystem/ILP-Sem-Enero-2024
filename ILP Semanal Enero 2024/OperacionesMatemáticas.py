# Operaciones Matemáticas (Suma, Resta, Multiplicación, División, Potencia, Raíz Cuadrada, Módulo)

# Importar librerías de funciones matemáticas
import math

# ENTRADA DE DATOS
número1 = float(input("Ingresa un número:")) # los input obtienen tipo de dato string
número2 = float(input('Ingresa otro número:'))

PI = 3.1416 # Declarar, crear o instanciar una Constante

# PROCESOS (Operaciones y/o cálculos matemáticos y lógicos)
suma = número1 + número2
resta = número1	- número2
multiplicación = número1 * número2
división = número1 / número2

potencia_1 = número1 ** número2 # 10 elevado a la potencia 5.7
potencia_2 = pow(número1, número2)
cuadrado = número1 ** 2
cubo = número2 ** 3

raíz_cuadrada_1 = math.sqrt(27)
raíz_cuadrada_2 = pow(27, 1/2)
raíz_cúbica = pow(27, 1/3)

módulo_residuo = número1 % número2

# SALIDA DE DATOS
print("La suma es =", suma)   # 1ra forma para imprimir
print("La suma es = " + str(suma)) # 2da forma para imprimir CONCATENAR: 
print(f"La suma es = {suma}") # 3ra forma para imprimir
print("La resta es =", resta)
print("La multiplicación es =", multiplicación)
print("La división es =", división)
print("La división es =", round(división, 4))
print("El cuadrado es =", cuadrado)
print("El cubo es =", cubo)
print("La potencia 1 es =", potencia_1)
print("La potencia 2 es =", potencia_2)
print("La raíz cuadrada 1 es =", raíz_cuadrada_1)
print("La raíz cuadrada 2 es =", raíz_cuadrada_2)
print("La raíz cúbica es =", raíz_cúbica)
print("El módulo es =", módulo_residuo)
