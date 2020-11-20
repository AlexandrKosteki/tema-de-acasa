a=eval(input("marimea 1="))
b=eval(input('marimea 2='))
c=eval(input("marimea 3="))
if(a<b+c) and (b<a+c) and (c<a+b):
    if(a==b) or (a==c) or (b==c):
        print("triunghiul este isoscel deoarece are doua laturi egale")
    if(a==b==c):
        print("triunghiul este eghilateral deoarece toate laturile sunt egale")
    else:
        print ("triunghiul este scalen")
else:
    print("nu corespunde cerintei")