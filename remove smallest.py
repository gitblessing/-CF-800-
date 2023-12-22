for testcases in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    ans = "YES"
    for i in range(1,n):
        if arr[i]-arr[i-1]>1:
            ans = "NO"
        else:
            continue
    if len(arr)==1:
        ans = "YES"
    print(ans)
