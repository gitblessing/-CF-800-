n = int(input(""))



f_x = 0
f_y = 0
f_z = 0
while n > 0:
    n = n-1
    inp = list(map(int,input().split()))
    f_x = f_x + inp[0]
    f_y = f_y + inp[1]
    f_z = f_z + inp[2]

if f_x == f_y == f_z == 0:
    print("YES")
else:
    print("NO")
    
