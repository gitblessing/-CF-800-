for testcases in range(int(input())):
    n = int(input())
    arr = list(input())
    m=[]
    ans = "YES"
    for i in range(n):
        if arr[i] not in m:
            m.append(arr[i])
        elif arr[i-1]==arr[i]:
            continue
        else:
            ans="NO"
            break
    print(ans)