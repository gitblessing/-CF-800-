import math 
for no_testcase in range(int(input())):
    n = int(input())
    ans = "NO"
    arr = list(map(int,input().split()))
    
    
    for i in arr:
        if (math.sqrt(i)).is_integer():
            pass
        else:
            ans = "YES"
            break
    print(ans)