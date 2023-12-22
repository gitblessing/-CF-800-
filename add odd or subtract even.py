n = int(input())
for i in range (n):
    a,b = map(int ,input().split())
    steps = 0
    if (b-a)==0:
        steps = 0
    elif (b-a)>0 and (b-a)%2==0:
        steps =2
    elif (b-a)>0 and (b-a)%2!=0:
        steps =1
    elif (b-a)<0 and (b-a)%2==0:
        steps =1
    elif (b-a)<0 and (b-a)%2!=0:
        steps = 2
        
        
    print(steps)
        
    