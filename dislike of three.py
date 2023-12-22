from fractions import Fraction
n = int(input(""))
lis =[]
while n>0:
    n-=1
    x = int(input())
    
    if x%3==0 or Fraction(x,3)==1/3 or Fraction(x,3)==2/3:
        continue
    else:
        lis.append(x)
        
    print(lis[-1])