num1 = int(input("inserta el primer numero: "))
num2 = int(input("inserta el segundo numero: "))
if num1 < num2:
    while num1 <= num2:
        if num1 % 2 == 0:
            print(num1)
        num1 = num1 + 1