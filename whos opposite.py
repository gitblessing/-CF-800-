for no_testcase in range(int(input())):
    a,b,c = map(int,input().split())
    n = 2*abs(b-a)
    if n==2:
        ans =-1
    elif c>n:
        ans=-1
        
    elif max(a,b)>n:
        ans=-1
        
    else:
        if c>(n/2):
            ans = c-(n/2)
        else:
            ans = c+(n/2)
    print(int(ans))