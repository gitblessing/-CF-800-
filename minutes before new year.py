n= int(input())
for i in range(n):
    h,m = map(int,input().split())
    min_gone = (h*60 +m)
    left = (24*60) - min_gone
    print(left) 