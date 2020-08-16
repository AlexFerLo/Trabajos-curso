print("Pulse t para calcular area de un triangulo, c para area de circulo")
a=input()

if  a=='t' or a=='T':
	print("Base")		
	base=input()
	
	print("Altura")
	altura=input()
	
	area=(float(base)*float(altura)/2)
	print ("Area del triangulo : ",area)
if  a=='c' or a=='C':
	print("Radio")
	radio=input()
	float(radio)
	pi=3.14159
	area=pi*float(radio)**2
	print ("Area del circulo : ",area)

    









