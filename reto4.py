# Initializing the variables.
contador=0
contadorNegativos=0

# Asking the user to input a number and if the number is negative it will add it to the counter.
while(contador<=20):
    numero=int(input("Digite numero: "))
    contador+=1
    if(numero<0):
        contadorNegativos+=1
        if(contador==20):
            print(f'El total de numeros negativos es:{contadorNegativos}')