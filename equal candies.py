for no_testcase in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    lis.sort()
    mini = lis[0]
    eat = 0
    for i in lis:
        if i>mini:
            eat +=(i-mini)
    print(eat)
    