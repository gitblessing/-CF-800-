import math
n = int(input())
ans=0
if n%2==0:
    ans= int(n/2)
else:
    ans = -1*(math.ceil(n/2))
print(int(ans))
    