print("Cantidad de numeros:")
a=float(input())

lista=[]
for i in range(0,a):
    print("Introduzca  numero")
    b=float(input())
    int(b)
    lista=lista+[b]
    if i>=1:
        if lista[i]<lista[0]:
            print ("El numero es menor que el primer elemento:",lista[0])