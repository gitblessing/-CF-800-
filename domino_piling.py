inp = list(map(int,input().split()))
area = inp[0]*inp[1]
no_tiles = 0
if area%2==0:
    no_tiles = area/2
else:
    no_tiles = (area-1)/2
print(int(no_tiles))
    