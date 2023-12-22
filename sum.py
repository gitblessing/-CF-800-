n = int(input(""))
while n>0:
    n-=1
    inp = list(map(int,input("").split()))
    inp = sorted(inp)
    a,b,c =inp[0],inp[1],inp[2]
    if c==a+b:
        print("YES")
    else:
        print("NO")