print ("Introduzca dos numaros");
a=int(input());
b=int(input());

if a<=0:
    print ("ERROR");
else :
    if b<=0:
        print ("ERROR");
    else :
        if a>b:
            divi=a/b;
            rest=a%b;
            if rest ==0:
                print (a,"es multiplo de",b);
            else :
                print (a,"no es multiplo de",b);
        else :
            divi=b/a;
            rest=b%a;
            if rest ==0:
                print (b,"es multiplo de",a);
            else :
                print (b,"no es multiplo de",a);

            









