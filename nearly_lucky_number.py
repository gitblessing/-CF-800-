str = input("")
lis = []
for i in str:
    lis.append(i)

lucky = 0

for i in lis:
    if i == '4' or i == '7':
        lucky +=1
    else:
        continue

if lucky == 7 or lucky == 4:
    print("YES")
else:
    print("NO")
     