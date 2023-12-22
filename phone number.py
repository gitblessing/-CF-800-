n = int(input())
nums = list(str(input()))
ans = 0
c_8 = nums.count('8')


while n>=11 and c_8>0:
    n-=11
    ans+=1
    c_8-=1

print(ans)