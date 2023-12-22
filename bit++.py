t = int(input(""))
x = 0
while t>0:
    t=t-1
    str = input("")
    str = str.lower()
    if str == '++x' or str=='x++':
        x = x+1
    if str == '--x' or str== 'x--':
        x = x-1

print(x)