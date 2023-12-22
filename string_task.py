str = input("").lower()
lis = []
vowels = ["a","e","i","o","u","y"]
for i in str:
    
    if i in vowels:
        continue
    else:
        lis.append(i)
        
print(".",end="")
print(*lis,sep=".")
