VariableContador = 0
while VariableContador <= 10:
    VariableNumerica = int(input("inserte la variable: "))
    if VariableNumerica >= 50:
        VariableContador = VariableContador + 1
        if VariableNumerica % 2 != 0:
            print(VariableNumerica)