a,b,c,d = map(int,input().split())
l = [a,b,c,d]
l.sort()
# a = x + y
# b = x + z
# c = y + z
# d = x + y + z
print(l[-1]-l[0],l[-1]-l[1],l[-1]-l[2],) 
