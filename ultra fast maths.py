str1 = input("")
str2 = input("")
lis =[]
for i in range (len(str1)):
    if str1[i] == str2[i]:
        lis.append('0')
    else:
        lis.append('1')

for j in lis:
    print(j,end="")
        