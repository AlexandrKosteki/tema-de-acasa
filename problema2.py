p=1
s=0
n=eval(input("n="))
if n>1:
    for i in range(1,n+1):
        p=p*i
        s=s+p
    print("suma=",s)
    