s = input("")
t = s.split()
count_lc = 0
count_uc = 0
for i in s:
    if i.isupper():
        count_uc += 1
    else:
        count_lc += 1 
if count_lc >= count_uc:
    s = s.lower()
    print(s)
else:
    s = s.upper()
    print(s)
    