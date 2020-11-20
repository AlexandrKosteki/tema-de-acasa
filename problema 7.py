v=eval(input("Virsta este="))
s=1
c=1
if v<20:
    for i in range (1, v+1):
        c=c*2
        s+=c+i
    print("Mihai are",s,"dolari la virsta",v,"ani")

s=1
i=0
c=1
while s<=100:
    i=i+1
    c=c*2
    s+=c+1
print("100 dolari a primit la",i,"ani")