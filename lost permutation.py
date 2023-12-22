t = int(input(""))
for a in range(t):
    m,s =map(int,input().split())
    inp = list(map(int,input().split()))
    inp.sort()
    possible = 0
    
    for b in range(1,inp[-1]+1):
        if b not in inp:
            inp.append(b)
            s-=b
    inp.sort()
    
    while s>0:
        s-=inp[-1]+1
        inp.append(inp[-1]+1)
        inp.sort()
    
    
    if s<0:
        possible = 0
    elif s==0:
        possible = 1
    
    if possible!=0:
        print("YES")
    else:
        print("NO")