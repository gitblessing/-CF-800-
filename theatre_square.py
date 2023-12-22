inp = list(map(int,input().split()))
n = inp[0]
m = inp[1]
a = inp[2]
print(n,m,a)
area = n*m
tile = a*a
count = 0

while area>tile:
    area = area/tile
    count+=1
print(count)
     
