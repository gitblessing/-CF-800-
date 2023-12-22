n = int(input())
ar = list(map(int,input().split()))
le = 1
l = [ar[x+1]-ar[x] for x in range(n-1) ]

coun = 1
for i in l:
    
    if i>0:
        coun+=1
        
    elif i<=0:
        coun = 1
    if coun>=le:
        le = coun
    
print(le)