num = int(input(""))
str_num = str(num)
allowed = ['1','4']
for i in str_num:
    if i not in allowed:
        print("NO")
        break
