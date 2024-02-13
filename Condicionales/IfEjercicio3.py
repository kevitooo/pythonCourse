#Ejercicio 3

nom = input("Enter the first name: ")
nom2 = input("Enter the second name: ")

if nom[0] == nom2[0] or nom[-1] == nom2[-1]:
    print("There's coincidence")
else:
    print("There's not coincidence")