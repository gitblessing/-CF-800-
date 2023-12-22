n = int(input(""))
str = input("").lower()
char = []
for i in str:
    if ord(i) >= 97 and ord(i) <= 122 and i not in char:
        char.append(i)   
    else:
        continue 

if len(char) >= 26:
    print("YES")
else:
    print("NO")  
