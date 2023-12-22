amt = int(input(""))
count = 0
while amt >= 0:     
    if amt-100 >= 0:
        count+=1
        amt = amt-100
        continue
    elif amt - 20 >= 0:
        count+=1
        amt-=20
        continue
    elif amt-10 >=0:
        count+=1
        amt-=10
        continue
    elif amt-5>=0:
        count+=1
        amt-=5
        continue
    elif amt-1>=0:
        count+=1
        amt-=1
        continue
    else:
        break
    

print(count)
    
