x = int(input(""))
ans = 0

while x>0:
    x=x-1
    inp = list(map(int,input().split()))
    key = sorted(inp)[-2]
    if key == 1:
        ans= ans+1
    
print(ans)
