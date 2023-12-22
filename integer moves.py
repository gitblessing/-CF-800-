import math
for no_testcase in range(int(input())):
    x,y  = map(int,input().split())
    if x==y==0 :
        moves =0 
    elif (math.sqrt((x**2 )+(y**2))).is_integer():
        moves = 1
    else:
        moves = 2
    print(moves)
         