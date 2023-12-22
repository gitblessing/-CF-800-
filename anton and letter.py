str = input("").lower()
ignore = ['{','}',' ',',']
lis = []
count = 0
for i in str: 
    if i in ignore or i in lis:
        lis.append(i)
        continue
    else:
        lis.append(i)
        count+=1
print(count)
