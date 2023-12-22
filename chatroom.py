st = input("")
allowed = ['h','e','l','l','o']
lis = []
j = 0
for i in st:
    if j==len(allowed):
        break
    elif i==allowed[j]:
        lis.append(i)
        j+=1
    else:
        continue
if lis == allowed:
    print("YES")
else:
    print("NO")