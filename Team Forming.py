n = int(input())
arr = sorted(list(map(int,input().split()))) 
count = 0 
for i in range(0,n,2):
    if arr[i]!=arr[i+1]:
        count+= arr[i+1]-arr[i]
print(count)