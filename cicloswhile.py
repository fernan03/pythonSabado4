observador=100


print("**MENU**")
print("0.SALIR")
print("1.SALUDAR")
print("2.DESPEDIR")
while(observador !=0):
    observador=int(input("Digite una opcion:"))
    if(observador==0):
        break
    elif(observador==1):
        print("Hola observador")
    elif(observador==2):
        print("Adios observador")
    else:
        print("Digite opcion valida")
else:
    print("ya no estoy aqui")
