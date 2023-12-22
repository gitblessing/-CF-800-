for testcases in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    m_c=0
    for i in arr:
        if i==-1:
            m_c +=1
    if m_c%2==0:
        ans = n
    else:
        ans = n-2
    print(ans)
