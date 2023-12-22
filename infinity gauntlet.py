have = 0
col = ['purple', 'green', 'blue', 'orange', 'red', 'yellow']
stones = [ 'Power','Time','Space','Soul','Reality','Mind']
for no_testcase in range(int(input())):
    
    n = input()
    t = col.index(n)
    
    col.pop(t)
    stones.pop(t)
    have+=1

print(6-have)
print(*stones,sep="\n")
    