num1 = int(input("inserte un numero: "))    
num2 = int(input("inserte otro numero: "))
num3 = int(input("inserte otro numero: "))   
print("busqueda del numero mayor") 
if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else: 
        print(num3)
print ("busqueda del numero menor")
if num1 < num2:
    if num1 < num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 < num3:
        print(num2)
    else:
        print(num3)