#Bucle while
import math

num = int(input("Ingrese un numero: "))

while num < 0:
    print("Por favor ingrese un numero positivo.")
    num = int(input("Vuelva a ingresar un numero positivo: "))

print(f"El resultado de la raiz cuadrada es: {math.sqrt(num):.2f}")