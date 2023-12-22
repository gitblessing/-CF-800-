amt = int(input(""))
count = 0
while amt >= 0:     
    if amt-5 >= 0:
        count+=1
        amt = amt-5
        continue
    elif amt - 4 >= 0:
        count+=1
        amt-=4
        continue
    elif amt-3 >=0:
        count+=1
        amt-=3
        continue
    elif amt-2>=0:
        count+=1
        amt-=2
        continue
    elif amt-1>=0:
        count+=1
        amt-=1
        continue
    else:
        break
    

print(count)
    
