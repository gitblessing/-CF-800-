t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    lights = 0
    if n>m:
        lights += (m*m)/2 
          