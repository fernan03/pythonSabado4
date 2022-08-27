numeros = int(input("Digite numero entero: "))

while(numeros>=0):
    sumaNumeros = numeros
    numeros = int(input("Digite numero entero: "))
    sumaNumeros = sumaNumeros + numeros
    print(f'La suma de los numeros es:{sumaNumeros}')
else:
    print(f'termine')

    #no terminado