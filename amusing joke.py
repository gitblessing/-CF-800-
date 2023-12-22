name1 = input("")
name2 = input("")
str = list(map(str,input("")))
lis=[]

for i in name1:
    lis.append(i)
for j in name2:
    lis.append(j)

lis.sort()
str.sort()

if str == lis :
    print("YES")
else:
    print("NO")
