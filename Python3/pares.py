print("Introduzca numero:")
a=int(input())
print("Introduzca numero:")
b=int(input())

par=[]
impar=[]

for i in range(a,b+1):
        if i%2==0:
            par=par+[i]
        else:
            impar=impar+[i]

print ("Numeros pares:",par);
print ("Numeros impares:",impar)