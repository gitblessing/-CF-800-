for no_testcase in range(int(input())):
    key  = int(input())
    inp = list(map(int,input().split()))
    key_got = [1,2,3]
    opened = []
    ans = 0
    
    for i in range(3):
        if key in key_got:
            key_got.remove(key)
            key = inp[key-1]
        if key ==0 and len(key_got)!=0:
            ans = "NO"
        elif key ==0:
            ans ="YES"
            
        if len(key_got)==0:
            ans = "YES"
            break
    
    print(ans)