for no_testcase in range(int(input())):
    x,y,z = map(int,input().split())
    ans = ""
    if x==y==max(x,y,z):
        b = x
        a = z
        c = z
    elif x==z==max(x,y,z):
        a = y
        b = x
        c = y 
    elif y==z==max(x,y,z):
        a = x
        b = x
        c = z
    else:
        ans= "NO"
    
    if ans =="NO":
        print("NO") 
    else:
        print("YES")
        print(a,b,c)       