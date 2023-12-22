str = input("")
lis =[]
new =[]
for i in str:
    lis.append(i)
for x in lis:
    if x not in new:
        new.append(x)
    else:
        continue
if len(new)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
 