for no_testcase in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(arr.count(1) + arr.count(3))