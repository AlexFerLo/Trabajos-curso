print("Cantidad de numeros:")
a=int(input())

lista=[]
listam=[]
y=0
z=0
for i in range(0,a):
    print("Introduzca  numero")
    b=int(input())
    int(b)
    lista=lista+[b]
    if i%2==0:
        lista=lista+[b]
        y=y+1
    else:
        ista=lista+[b]
        z=z+1
print (y,"pares",z,"impares")