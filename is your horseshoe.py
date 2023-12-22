str = input("").split()

lis = []
for i in str:
    if i in lis:
        continue
    else:
        lis.append(i)
print(4-len(lis))