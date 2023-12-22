for testcases in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if len(set(arr)) == 1:
        print(0)
    else:
        print(n-arr.count(min(arr)))
