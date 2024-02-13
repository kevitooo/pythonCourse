#Exercice 4

yourbal = 2000
print("1. Deposit cash")
print("2. Withdrawal cash")
print("3. Show cash")
print("4. Exit")

num = int(input("Enter any option: "))

if num == 1:
    add = float(input("how much money do you want to deposit?: "))
    yourbal += add
    print(f"Your new balance: {yourbal}")
elif num == 2:
    wdr = float(input("how much money do you want to withdrawal?: "))
    if wdr > yourbal:
        print("Insufficient balance")
    else:
        yourbal -= wdr
        print(f"Your new balance: {yourbal}")
elif num == 3:
    print(f"Your balance: {yourbal}")
elif num == 4:
    print("Good bye")
else:
    print("Error 404")