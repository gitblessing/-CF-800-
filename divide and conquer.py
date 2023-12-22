# CODE CORRECT BUT TIME COMPLEXITY PROBLEM

import math 
for no_testcase in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    move=0
    even=0
    if sum(lis)%2==0:
        move+=0
    else:
        while sum(lis)%2!=0:
            for i in range(len(lis)):
                if lis[i]%2==0:
                    lis[i] = int(lis[i]/2)
                    move+=1
                
                for j in lis:
                    if j%2==0:
                        even+=1 
                       
                if lis[i]%2!=0 and even==0:
                    lis[i]= int(math.floor(lis[i]/2))
                    move+=1
                if sum(lis)%2==0:
                    break
                
                else:
                    continue
        
    
    print(move)