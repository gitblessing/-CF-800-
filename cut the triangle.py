
def check(x1,y1,x2,y2,x3,y3):
    a=0
    if x1 in range(x2+1,x3) :
        a +=1
    elif y1 in range(y2+1,y3):
        a +=1
    return a


for no_testcase in range(int(input())):
    t = input()
    ans,a=0,0
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    
    
    
    ans+=check(x1,y1,x2,y2,x3,y3)
    ans+=check(x1,y1,x3,y3,x2,y2)
    ans+=check(x2,y2,x1,y1,x3,y3)
    ans+=check(x2,y2,x3,y3,x1,y1)
    ans+=check(x3,y3,x1,y1,x2,y2)
    ans+=check(x3,y3,x2,y2,x1,y1)
    
    if ans>=1:
        print("YES")
    else:
        print("NO")