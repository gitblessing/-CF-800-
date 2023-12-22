for no_testcase in range(int(input())):
    
    a,b=map(int,input().split())
    t=1
    for i in range (0,b+1):
        for j in range (0,a+1):
            if 1*j +2*i == t:
                t+=1
        
        
    
    
          
    print(t)