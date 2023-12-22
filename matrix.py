str1 = input("").lower()
str2 = input("").lower()
length = len(str1)

val = 0
x = len(str1)
while x>0:
    x =x-1
    i=0
    while str1[i] != str2[i]:
        i=i+1
        continue
    if ord(str1[i]) > ord(str2[i]):
            val = 1
    elif ord(str1[i]) < ord(str2[i]):
            val = -1  
    
print(val)