for no_testcase in range(int(input())):
    n = int(input())
    allow = ['T','i','m','u','r']
    allow.sort()
    st = input()
    l=[]
    for i in st:
        l.append(i)
    l.sort()
    if l==allow:
        print("YES")
    else:
        print("NO")