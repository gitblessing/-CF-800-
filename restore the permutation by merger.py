for no_testcase in range(int(input())):
    n = int(input())
    lis=list(map(int,input().split()))
    l1,l2=[],[]
    for i in lis:
        if i not in l1:
            l1.append(i)
        else:
            l2.append(i)
    print(*l1)