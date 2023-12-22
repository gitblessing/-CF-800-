for no_testcase in range(int(input())):
    n = int(input())
    inp = list(map(int,input().split()))
    inp.sort()
    ans = 0
    t = True
    if n ==1 and inp[0]>1:
        ans = "NO"

    elif n==1:
        ans = "YES"
    
    elif inp[-1]-inp[-2]>=2 and n>2:
        ans = "NO"
    
    else:
        ans = "YES"
    print(ans)