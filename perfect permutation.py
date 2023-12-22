import random
n =int(input())
if n%2==0:
    l = [x for x in range(1,n+1)]
    for j in range(0,n,2):
        l[j],l[j+1]=l[j+1],l[j]
    print(*l,sep=" ")
elif n%2!=0:
    print(-1)