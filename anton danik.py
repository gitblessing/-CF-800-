n = int(input(""))
str = input("")
anton = 0
danik = 0

for i in str:
    if i == 'A':
        anton +=1
    else:
        danik +=1 
if anton == danik:
    print("Friendship")
elif anton > danik:
    print("Anton")
else:
    print("Danik")