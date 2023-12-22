n = int(input(""))
while n>0:
    n-=1
    j=0
    inp1 = list(map(int,input("").split()))
    inp2 = list(map(int,input("").split()))
    x,y = inp1[0],inp1[1]
    for i in inp2:
        j = j+i
  
    if j>=y:
        print(j-y)
    else:
        print("0")
        
    
    