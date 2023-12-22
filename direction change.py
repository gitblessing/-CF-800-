for no_testcase in range(int(input())):
    n,m=map(int,input().split())
    ini = [1,1]
    ans = 0
    if n==1 and m>2:
        ans +=1
        
    elif m==1 and n>2:
        ans +=1
        
    elif n==1 and m==1:
        step = 0
    else:   
        for i in range(n*m):
            if i%2==0:
                if ini[1]<m:
                    ini[i]=ini[i]+1
                    step+=1
                elif ini[1]==m:
                    step+=1
                    ini[i]=ini[i]-1
            else:
                if ini[0]<n:
                    step+=1
                    ini[i]=ini[i]+1
                elif ini[0]==n:
                    ini[i]=ini[i]-1 
                    step+=1
    print(ini)            
    if ans>=1:
        print(-1)
    else:
        print(step)