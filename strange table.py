import math
for no_testcase in range(int(input())):
    n,m,k = map(int,input().split())
    
    i = math.ceil(k/n)
    if k%n==0:
        j=n
    else:
        j = k%n
    
    print( (j-1)*m + i )