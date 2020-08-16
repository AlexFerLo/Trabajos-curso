print("Cantidad de numeros:")
a=int(input())

lista=[]
listam=[]
y=0

for i in range(0,a):
    print("Introduzca  numero")
    b=float(input())
    
    lista=lista+[b]
    if b<0:
        
        listam=listam+[b]
        y=y+1
print (y,listam)