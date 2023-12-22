import math 
for no_testcase in range(int(input())):
    n = int(input())
    inp = list(map(int,input().split()))
    avg = math.ceil(int(sum(inp))/n)
    print(avg)