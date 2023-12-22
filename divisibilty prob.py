import math 
for no_testcase in range(int(input())):
    a,b = map(int,input().split())
    
    if a>b:
        move = b*math.ceil(a/b)-a
    elif a%b==0:
        move =0
    elif a<b:
        move = b-a
    else:
        move = -1
    print(move)  
        
        