n = int(input(""))
sub,count,i = 0,0,1
left = n

while left>=sub :
    sub = int(i*(i+1)/2)
    left-=sub
    if left<0:
        break
    else:
        count+=1
        i+=1
    
print(count)