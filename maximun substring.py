n = int(input(""))
while n>0:
    n-=1
    t =int(input(""))
    str = input("")
    lis =[]
    for i in str:
        lis.append(i)
        continue
    
    a = lis.count('1')
    b = lis.count('0')
    x = "1"*a
    y = "0"*b
    
    if a == 0:
        print(b**2)
    elif b ==0:
        print(a**2)
    elif x in str and len(x)>len(y):
        print(a**2)
    elif y in str:
        print(b**2)   
    else:
        print(a*b)