n = int(input(""))
while n>0:
    n-=1
    fin1,fin2 =0,0
    lis = list(map(int,input().split()))
    if lis[0] > lis[1]:
        fin1 = lis[0]
    else:
        fin1 = lis[1]
        
    if lis[2]>lis[3]:
        fin2 = lis[2]
    else:
        fin2=lis[3]
        
    newlis = sorted(lis)
    t,z = [],[]
    t.append(newlis[-2])
    t.append(newlis[-1])
    
    z.append(fin1)
    z.append(fin2)
    z = sorted(z) 
    
   
    
    if z == t:
        print("YES")
    else:
        print("NO")   