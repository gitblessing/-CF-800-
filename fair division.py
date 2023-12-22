for no_testcase in range(int(input())):
    n = int(input())
    arr= list(map(int,input().split()))
    count_1 = arr.count(1)
    count_2 = arr.count(2)
    
    if count_1==0 :
        if count_2%2==0:
            print("YES")
        else:
            print("NO")
    
    elif count_2==0 :
        if count_1%2==0:
            print("YES")
        else:
            print("NO")
    
    elif count_1%2==0 and count_2%2==0:
        print("YES")
    elif count_1%2!=0 and count_2%2==0:
        print("NO")
    elif count_1%2==0 and count_2%2!=0:
        print("YES")
    elif count_1%2!=0 and count_2%2!=0:
        print("NO")
    else:
        print("OTHER CASE")