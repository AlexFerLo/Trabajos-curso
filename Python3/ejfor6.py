print("Cantidad de numeros:")
a=int(input())

lista=[]
listam=[]
suma=0

for i in range(0,a):
    print("Introduzca el numero")
    b=input()
    int(b)
    lista=lista+[b]
    suma=suma+int(lista[i])
print ("La suma es : ",suma)