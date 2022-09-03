# Asking the user to input a number.
numero = int(input("Digite numero entero: "))
# Initializing the variable `suma` to 0.
suma=0
# Asking the user to input a number and then it is adding the number to the suma variable.
while(numero>=0):
    suma = suma+numero
    print(f'La suma de los numeros es:{suma}')
    numero = int(input("Digite numero entero: "))
else:
    print(f'termine')

    