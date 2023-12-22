a , b = (input("")).split()
a,b = int(a),int(b)
row = 0


inp = list(map(int,input().split()))
for i in inp:
    if i >b:
        row +=2
    else:
        row +=1 
    
print(row)