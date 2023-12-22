for no_testcase in range(int(input())):
    n,m = map(int,input().split())

    for i in range(1,m+1,2):
        n-=i
        print(n)
    
    if n==0:
        print("YES")
    else:
        print("NO")