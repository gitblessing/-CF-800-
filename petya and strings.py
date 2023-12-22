str1 = input("").lower()
str2 = input("").lower()
n=0
for i in range (len(str1)):
    if n!=0:
        break
    elif str1[i] == str2[i]:
        continue
    elif str1[i] > str2[i]:
        n +=1
        break
    else: 
        n-=1
        break
print(n)