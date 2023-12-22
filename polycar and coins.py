import math
n = int(input(""))
rs1,rs2 =0,0

while n>0:
    x,z,rs1,rs2,t=0,0,0,0,0
    n-=1
    x = int(input(""))
    t = x
    z = math.floor(x/3)
    x = z
    if t-3*(x) == 2:
        rs2+=1
        
    elif t-3*(x) == 1:
        rs1+=1
        
    rs1+=z
    rs2+=z
    print(rs1,rs2)