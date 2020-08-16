print ("Introduzca año actual");
a=input();
print ("Introduzca año aleatorio");
b=input();
int(a)
int(b)

if a<b :
    an=(int(b)-int(a));
    if an ==1:
        print ("Falta",an,"año");
    else :
        print ("Faltan",an,"años");

else :
    an=(int(a)-int(b));
    if an ==1:
        print ("Ha pasado",an,"año");
    else :
        print ("Han pasado",an,"años");