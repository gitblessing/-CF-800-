import math
for testcases in range(int(input())):
    a,b =(map(int,input().split()))

    
    step = 0
    
    t = abs(b-a)
    t = t/10
    if t==0:
        step = 0 
    else:
        step+=math.ceil(t)

    print(step)        