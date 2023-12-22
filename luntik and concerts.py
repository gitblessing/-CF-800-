for no_testcase in range(int(input())):
    a,b,c = map(int,input().split())
    length = a + b*2 +c*3
    if length%2==0:
        ans = 0
    else:
        ans = 1
    print(ans)