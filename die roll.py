from fractions import Fraction
inp = list(map(int,input().split()))
a,b = inp[0],inp[1]

if a>b:
    i,j=a,b
else:
    i,j =b,a

if i==j==1:
    prob = '1/1'
elif i>j and i==2:
    prob = Fraction(5,6)
elif i>j and i==3:
    prob = Fraction(2,3)
elif i>j and i==4:
    prob = Fraction(1,2)
elif i>j and i==5:
    prob = Fraction(1,3)
elif i>j and i ==6:
    prob = Fraction(1,6)
elif i==j:
    prob = Fraction(7-i,6)
else:
    prob = 0

print(prob)