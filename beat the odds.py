n =int(input(""))
while n>0:
    n-=1
    x =int(input(""))
    even,odd =[],[]
    inp = list(map(int,input().split()))
    for j in inp:
        if j%2==0:
            even.append(j)
        else:
            odd.append(j)
    if len(even)>len(odd):
        print(len(odd))
    else:
        print(len(even))
        