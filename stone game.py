for testcases in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    hf = arr.index(max(arr))+1
    lf = arr.index(min(arr))+1
    hb = n-arr.index(max(arr))
    lb = n-arr.index(min(arr))

    steps=0

    

    