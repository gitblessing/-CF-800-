s = input()
t = input()
j,step=0,1
for i in t:
    if i==s[j]:
        step+=1
        j+=1
print(step)