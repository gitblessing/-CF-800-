for no_testcase in range(int(input())):
    a,b,c,x,y = map(int,input().split())
    
    x-=a
    y-=b
    
    if x>0 and c>=x:
        c-=x
        x = 0
    if y>0 and c>=y:
        c-=y
        y=0
    
    
    if x<=0 and y<=0 and c>=0:
        print("YES")
    else:
        print("NO")
        