print ("evaluacion de numero menor")
num1 = int(input("inserte un numero: "))
num2 = int(input("inserte otro numero: "))
num3 = int(input("inserte otro numero: "))
num4 = int(input("inserte otro numero: "))
if num1 < num2:
	if num1 < num3:
		if num1 < num4:
			print(num1)
		else:
			print(num4)
	else:
		if num3 < num4:
			print(num3)
		else:
			print(num4)
else:
	if num2 < num3:
		if num2 < num4:
			print(num2)
		else:
			print(num4)
	else:
		if num3 < num4:
			print(num3)
		else:
			print(num4)
