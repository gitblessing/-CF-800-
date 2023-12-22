for testcases in range(int(input())):
    n = int(input())

    if n==1 or n==2 :
        ans = 0
    elif n%2==0:
        ans = int((n-2)/2)
    else: 
        ans = int((n-1)/2)
    print(ans)