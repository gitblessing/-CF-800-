st = input()
st2 = input()
l = list(st)
lis = list(st2)

if l[0] in lis:
    print("YES")
elif l[1] in lis:
    print("YES")
else:
    print("NO")