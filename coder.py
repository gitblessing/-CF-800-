import math
n = int(input())
print(math.ceil(n/2))
for i in range(n):
    
    for  j in range(n):
        if i%2==0:
            if j%2==0:
                print("C",end="")
            else:
                print(".",end="")
            if j==n-1:
                break
        else:
            if j%2==0:
                print(".",end="")
            else:
                print("C",end="")
            if j==n-1:
                