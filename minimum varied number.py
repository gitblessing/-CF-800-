for no_testcase in range(int(input())):
    n = int(input())
    ans = 0
    
    if n==45:
        ans = 123456789
    elif n<45 and n>=42:
        ans = 3456789 + (n-42)*10000000
    elif n<42 and n>=39:
        ans = 456789 +  (n-39)*1000000     
    elif n<39 and n>=35:
        ans = 56789 +  (n-35)*100000 
    elif n<35 and n>=30:
        ans = 6789 +  (n-30)*10000 
    elif n<30 and n>=24:
        ans = 789 +  (n-24)*1000 
    elif n<24 and n>=17:
        ans = 89 +  (n-17)*100
    elif n<17 and n>=9:
        ans = 9 +  (n-9)*10
    elif n<=9 :
        ans = n
    print(ans)
    
    