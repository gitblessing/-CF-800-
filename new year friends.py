inp = list(map(int,input().split()))
inp = sorted(inp)
a,b,c = inp[0],inp[1],inp[2]
t = (b-a) + (c-b)
print(t)