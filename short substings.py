n = int(input(""))
while n>0:
    n-=1
    lis =[]
    inp = str(input(""))
    for i in range(0,len(inp)-1):
        if inp[i] != inp[i+1]:
            lis.append(inp[i])
            i+=2
        else:
            i+=2
            continue
    z = inp[-1]
    lis.append(inp[-1])
   
    print(*lis,sep='')
        
        
    
        
        