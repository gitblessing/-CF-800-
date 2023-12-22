for no_testcase in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    su = sum(arr)
    ones,zeros = arr.count(1),arr.count(0)
    ans = 0 
    