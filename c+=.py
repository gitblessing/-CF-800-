for no_testcase in range(int(input())):
    a,b,n = map(int,input().split())
    co = 0
    while n>=a and n>=b:
        
        if co%2==0:
            a+=b
            co+=1
            
        elif co%2!=0:
            b+=a
            co+=1
            
        if n<a or n<b:
            break
            
       
    print(co)