
num=int(input())
hor=(num//3600)
minu=(num-(hor*3600))//60
seg=num-((hor*3600)+(minu*60))
print (hor,"h",minu,"m",seg,"s");




