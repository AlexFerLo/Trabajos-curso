print ("Introduzca dos numaros");
a=int(input());
b=int(input());


if b==0:
    print ("No se puede divdir por 0");
else:
    divi=a/b;
    if a<b :
        print ("La division no es exacta")
    else:
        print (divi);
        rest=a%b;
        if rest!=0:
            print ("La division no es exacta")
         

