n = int(input(""))
while n>0:
    n-=1
    x = int(input(""))
    lis = []
    inp = list(map(str,input("").split()))
    for j in inp:
        if j not in lis:
            lis.append(j) 
            