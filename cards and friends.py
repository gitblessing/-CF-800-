for no_testcase in range(int(input())):
    w,h,n = map(int,input().split())
    card=0
    w_count,h_count=1,1
    
    if w%2!=0 and h%2!=0:
        card = 1
    
    elif w==1 and h%2==0:
        card = h
    elif h==1 and w%2==0:
        card = w
        
    else:
        
        while w%2==0:
            w=w/2
            w_count+=1
        
        while h%2==0:
            h= h/2
            h_count+=1
        
        card+=1
    
    
    if card>=n:
        print("YES")
    elif card<n:
        print("NO")
   