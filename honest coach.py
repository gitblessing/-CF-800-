for no_testcase in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    l=[]
    for i in range(0,n-1):
        l.append(arr[i+1]-arr[i])
    
    print(min(l))