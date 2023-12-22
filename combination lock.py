n = int(input())
curr = input()
og = input()
move=0
curr_l = [int(x) for x in curr]
og_l = [int(x) for x in og]
for i in range(n):
    if og_l[i]==curr_l[i]:
        pass
    else:
        move += min(abs(curr_l[i]-og_l[i]) ,(min(abs(curr_l[i]-0),abs(curr_l[i]-9)) + 1 + min(abs(og_l[i]-0),abs(og_l[i]-9)) ) )
    
print(move)