n= int(input(""))
while n>0:
    n-=1
    inp = list(map(int,input().split()))
    a,b,c,d =inp[0],inp[1],inp[2],inp[3]
    count = 0 
    for i in range(1,len(inp)):
        if inp[i]>a:
            count+=1
        else:
            continue
    print(count)