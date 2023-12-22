n = int(input(""))
inp = list(map(int,input("").split()))
inp = sorted(inp)
t = inp[-1]
count = 0
for j in inp:
    if j<t:
        count+=(t-j)
    else:
        continue
print(count)
    