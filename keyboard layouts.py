kb1 = str(input())
kb2 = str(input())
text = str(input())

ans= []


for j in text.lower():
    if j.isnumeric():
        ans.append(j)
        continue
    else:
        ans.append(kb2[kb1.index(j)])

pos = 0
for i in text:
    if i.isupper():
        ans[pos] = ans[pos].capitalize()
    
    pos+=1   
    

    
print(*ans,sep="")