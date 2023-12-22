n,d = map(int, input().split())
inp = list(map(int,input().split()))
i=0
count = 0
while d>0:
    if i>=len(inp)-1 and d>0:
        break 
    elif i==len(inp)-1 and d<=0:
        count=0
        break 
    else:
        d = d-inp[i]
        i+=1
        if d>=10:
            count+=2
        elif d<5:
            count+=0
        else:
            count+=1

if count==0:
    print(-1)
else:
    print(count)
    
