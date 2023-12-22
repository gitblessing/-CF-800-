for no_testcase in range(int(input())):
    a,b,c = (map(int,input().split()))
    
    if a == 1:
        t_a = 0
    elif a>1:
        t_a = a-1
    
    t_b = abs(b-c)
    t_b += c-1
    
    if t_a==t_b:
        print(3)
    elif t_a>t_b:
        print(2)
    elif t_a<t_b:
        print(1)
        
    