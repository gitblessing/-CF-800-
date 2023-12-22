import math 
for no_testcase in range(int(input())):
    year = int(input())
    ans = "NO"
    
    
    for x in range(0,math.ceil(year/2020)+5):
        for j in range (0,math.ceil(year/2020)):
            if 2020*j +2021*x ==year:
                ans = "YES"
                break
        
    print(ans)