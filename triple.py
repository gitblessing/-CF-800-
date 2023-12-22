import collections 
for no_testcase in range(int(input())):
    n = int(input())
    inp = list(map(int,input().split()))
    inp.sort() 
    frequency = {}
    for item in inp:

        if item in frequency:
            # incrementing the counr
            frequency[item] += 1
        else:
            # initializing the count
            frequency[item] = 1
    result = {key:value for (key, value) in frequency.items() if value >= 3}
  
    if len(result)!=0:
        print(list(result.keys())[0])
    else:
        print(-1)