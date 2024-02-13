#Ejercicio 2

num = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if num >= num2 and num >= num3:
    print(f"The {num} is greater than all.")
elif num2 >= num and num2 >= num3:
    print(f"The {num2} is greater than all.")
elif num3 >= num and num3 >= num2:
    print(f"The {num3} is greater than all.")