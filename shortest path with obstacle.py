for no_testcase in range(int(input())):
    t = input()
    x1,y1=map(int,input().split()) # A
    x3,y3=map(int,input().split()) # B
    x2,y2=map(int,input().split()) # F
    
    steps = 0
    if x1==x2==x3 and y2 in range(min(y1,y3),max(y1,y3)):
        steps = abs(y3-y1) +2
    elif y1==y2==y3 and x2  in range(min(x1,x3),max(x1,x3)):
        steps = abs(x3-x1) +2
    elif x1==x2==x3 and y2 not in range(min(y1,y3),max(y1,y3)):
        steps = abs(y3-y1) 
    elif y1==y2==y3 and x2  not in range(min(x1,x3),max(x1,x3)):
        steps = abs(x3-x1) 

    else:
        steps = abs(x3-x1) + abs(y3-y1)
    print(steps)
    