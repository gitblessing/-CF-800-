n = int(input())
rows, cols = (n, n)
arr = [[0]*cols]*rows
for i in range(n):
    arr[0][i]=5
print(arr)