for no_testcase in range(int(input())):
    P = int(input())
    ans= []
    for j in range(2,P):
        r = P%j
        if (P/(P-2)).is_integer() and int(P/(P-2)) <=P:
            ans = [j,int(P/(P-2))]
    
    print(*ans,sep="")