for testcases in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    arr.sort()
    avg = arr[-1] + (sum(arr)-arr[-1])/(n-1)
    print(avg)