#Ejercicio 1

numero = int(input("Ingrese 1er numero: "))
numero2 = int(input("Ingrese 2do numero: "))

if numero % 2 == 0 and numero2 % 2 == 0:
    print("Son pares")
elif numero % 2 == 0 and numero2 % 2 != 0:
    print(f"{numero} es par")
elif numero % 2 != 0 and numero2 % 2 == 0:
    print(f"{numero2} es par")
else:
    print("Los dos numeros son impares")
