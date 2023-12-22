import math 
t = int(input(""))
for j in range(t):
    x,n,m= map(int,input().split())

    
    if x<=10 and m>=1:
        print("YES")
    
    else:
        for a in range(n):
            x = math.floor(x/2) + 10
            if x<=10:
                break
            else:
                continue
        
        for b in range(m):
            x = x-10
        if x<=0:
            print("YES")
        else:
            print("NO")