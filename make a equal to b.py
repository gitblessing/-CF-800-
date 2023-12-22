n = int(input(""))
while n>0:
    n-=1
    x =int(input(""))
    move = 0
    changes = 0
    inp1 = list(map(int,input().split()))
    inp2 = list(map(int,input().split()))
    if inp1==inp2:
        move=0
    else:   
    
        for i in range(len(inp1)):
            if inp1[i]==inp2[i]:
                continue
            else:
                changes+=1
        
        inp1,inp2 = sorted(inp1),sorted(inp2)
        move+=1
        a = inp1.count(0)
        b = inp2.count(0)
        if a == b:
            move = move
        else:
            if a>b:
                move+=(a-b)
            else:
                move+=(b-a)
    
        print(move,"-",changes)
    