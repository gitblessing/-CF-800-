n = int(input())
while n>0:
    n-=1
    z = int(input())
    inp =list(map(int,input().split()))
    a = 0
    count_t = 0
    x = 0
    t = inp[0]
    j=0
    for i in range (1,len(inp)):
        if inp[j] ==inp[i]:
            j+=1
            count_t+=1
            continue
        elif inp[j] !=inp[i]:
            x = j+1
            a = inp[j]
            j+=1
    print(inp[x])   
            
        