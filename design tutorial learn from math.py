import sympy

n =int(input(""))

if n%2==0:
    a,b = int(n/2),int(n/2)
    print(a,b)
elif n%2!=0:
    for i in range (n):
        x = n-i
        if sympy.isprime(x) == True or sympy.isprime(i) == True:
            continue
        else:
            break 
        print(x,i)    