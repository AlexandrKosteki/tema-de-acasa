from fractions import Fraction
a=eval(input("Numaratorul 1="))
b=eval(input("Numitorul 1="))
c=eval(input("Numaratorul 2="))
d=eval(input("Numaratorul 2="))
suma= Fraction(a,b)+Fraction(c,d)
produsul=Fraction(a,b)*Fraction(c,d)
print("suma=",suma)
print("produsul=",produsul)