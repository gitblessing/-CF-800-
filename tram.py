n = int(input(""))
curr = 0
max = 0 
while n>0:
    n -= 1
    a,b = (input("")).split()
    a,b = int(a),int(b)
    curr = curr + b - a
    
    if curr > max:
        max = curr

if curr == 0:
    print(max)