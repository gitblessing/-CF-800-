n = int(input())
arr = list(map(int,input().split()))

mx = arr[0]
mi = arr[0]
ans = [arr[0]]
aw = 0
for i in arr[1:]:
    if i>mx:
        aw +=1
        mx = i
    elif i<mi:
        aw+=1
        mi=i
print(aw)