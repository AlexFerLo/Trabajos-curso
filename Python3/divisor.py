print("Introduzca un numero")
a=input()
int(a)
divisor=[]
if int(a)>0:
    for i in range(1,int(a)+1):
        if int(a)%i==0:
            divisor=divisor+[i]
    print ("Los divisores son ",divisor)
else:
    print ("El numero debe ser mayor que 0")