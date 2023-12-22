import math
for no_testcase in range(int(input())):
    n = input()
    n1 = int(n)
    
    li = [0,2,4,6,8,10,12,14,16,18]
    l = int(n[-1])
    
    if n1%7==0:
        ans = n1
    
    else:
        for j in li:
            if 10<=n1<20:
                ans = 14
            elif 20<=n1<30:
                ans = 21
            elif 30<=n1<40:
                ans = 35
            elif 40<=n1<50:
                ans = 42
            elif 50<=n1<60:
                ans = 56
            elif 60<=n1<70:
                ans = 63
            elif 70<=n1<80:
                ans = 77
            elif 80<=n1<90:
                ans = 84
            elif 90<=n1<100:
                ans = 91
        
            
            elif (math.floor(n1/10) - j)%7==0:
                ans = (math.floor(n1/10))*10 + li.index(j)
                break
    print(int(ans))