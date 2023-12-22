n = int(input())
str = input()
coun = 0
step = 0
for i in str:
    if i=='x':
        coun+=1
    else:
        coun = 0 
    if coun>=3:
        step +=1
print(step)