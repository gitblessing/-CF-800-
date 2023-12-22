inp = input("").split()


a = (inp[0])
b = (inp[1])
a = int(a)
b = int(b)
count = 0
   
while b>=a:
    count=count+1
    a = a*3
    b = b*2
    
print(count)
