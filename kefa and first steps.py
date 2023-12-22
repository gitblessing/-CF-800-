n = int(input(""))
inp = list(map(int,input("").split()))
j=0
coun = 0
for i in range(1,len(inp)):
    if inp[j] <= inp[i]:
        coun +=1
        
    else:
        continue
    j+=1
print(coun)