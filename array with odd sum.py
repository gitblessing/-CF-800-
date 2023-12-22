for no_testcase in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    ans,odd,even = 0,0,0
    if sum(lis)%2==0:
        ans ="YES"
    for i in lis:
        if i%2!=0:
            odd+=1    
        else:
            even+=1
    
    if len(lis)%2!=0 and odd==len(lis):
        ans = "YES"
    elif len(lis)%2!=0 and even == len(lis):
        ans = "NO"
    elif len(lis)%2!=0 and odd>=1:
        ans ="YES"
    elif len(lis)%2==0 and odd>=1 and even>=1:
        ans = "YES"
    elif len(lis)%2==0 and odd==len(lis):
        ans = "NO"
    elif len(lis)%2==0 and even == len(lis):
        ans = "NO"
    else:
        ans = "OTHER CASE"
        
    print(ans)