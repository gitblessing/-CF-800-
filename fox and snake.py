m, n = map(int, input().split())
j=0
for i in range (1,m+1):
    if i != 2:
        print("#"*n)
        j+=1
    else:
        if j%2==0:
            print("."*(n-1))   
        else:
            print("#","."*(n-1),sep="")