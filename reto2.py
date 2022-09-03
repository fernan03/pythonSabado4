# Importing the math module.
import math
# Declaring the variables.
observador=100
modulo=None
raizCuadrada=None
suma=100
elevado=None
# Printing the menu.
print("..............")
print(".....MENU.....")
print("..............")
print("0.Salida")
print("1.Encuentre si el numero es multiplo de 2")
print("2.Encuentre la raiz cuadrada del numero")
print("3.Sumar 100 al numero ingresado")
print("4.Eleve a la 2 el numero ingresado")

# A while loop that will keep asking for an option until the user enters 0.
while(observador !=0):
    opcion = int(input("Digite opcion:"))
    if(opcion==0):
        print("Fin programa")
        break
    else:
        numero = int(input("Digite un numero:"))
        if(opcion==1):
            modulo=numero%2
            if(modulo==0):
                print(f'El numero {numero} es multiplo de 2')
            else:
                print(f'El numero {numero} no es multiplo de 2, su residuo es: {modulo}')
        elif(opcion==2):
            raizCuadrada=math.sqrt(numero)
            print(f'La raiz cuadrada de {numero} es {raizCuadrada}')
        elif(opcion==3):
            suma=suma+numero
            print(f'La suma de 100 y {numero} es {suma}')
        elif(opcion==4):
            elevado=numero**2
            print(f'El cuadrado de {numero} es {elevado}')
        else:
            print("Digite opcion valida")
        

    
