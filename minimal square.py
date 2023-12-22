n = int(input(""))
while n>0:
    n-=1
    inp = list(map(int,input().split()))
    a,b =inp[0],inp[1]
    sq = (2*a)*b
    l =(2*a)**2
    w =(2*b)**2
    
    s = 1
    t = 0
    while t<sq:
        s+=1
        t = s**2
    print(t)
        