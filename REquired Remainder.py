import math
n = int(input(""))
while n>0:
    n-=1
    inp =list(map(int,input().split()))
    x,y,d =inp[0],inp[1],inp[2]
    t = math.floor((d-y)/x)
    z = ((t*x) + y)
    print(z)