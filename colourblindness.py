for no_testcase in range(int(input())):
    n = int(input())
    l1 = list(input())
    l2 = list(input())
    ans = 0
    
    for i in range(n):
        if l1[i]==l2[i]:
            ans+=0
            pass
        elif l1[i]=='G' and l2[i]=='B':
            ans+=0
            pass
        elif l1[i]=='B' and l2[i]=='G':
            ans+=0
            pass
        else:
            ans+=1
        
    if ans!=0:
        print("NO")
    else:
        print("YES")