n = int(input())
ways = 0

for i in range(1,n+1):
    t=n-i
    if t%i==0:
        ways+=1
    else:
        continue
print(ways-1)
