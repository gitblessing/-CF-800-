n = int(input(""))
aval = 0
while n>0:
    n-=1
    inp = list(map(int,input("").split()))
    if ( inp[1] - inp[0] ) >= 2:
        aval +=1
    else: 
        continue  
    
print(aval)