for no_testcase in range(int(input())):
    n,m = map(int,input().split())
    arr_a = list(map(int,input().split()))
    arr_b = list(map(int,input().split()))
    
    c = list(set(arr_a).intersection(set(arr_b)))
    c.sort()
    
    if len(c)==0:
        print("NO")
    else:
        print("YES")
        print(1,c[0])