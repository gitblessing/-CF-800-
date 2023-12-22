for no_testcase in range(int(input())):
    n = input()
    inp =list(map(int,input().split()))
    inp.sort()
    s1,s2,neg,summ = 0,[],[],0
    for i in inp:
        if i<0:
            neg.append(i)
    if len(neg)!=0:
        s2.append(neg[-1])
        s1 = sum(inp)-neg[-1]
    else:
        s1 = sum(inp)
    t_s2 = sum(s2)
    if t_s2<0:
        t_s2*=(-1)
    
    if s1<0:
        s1*=(-1)
        
        
    final_sum = (s1-t_s2)
    print(final_sum)
    print(s2,t_s2,s1)
        
        