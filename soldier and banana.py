
inp = list(map(int,input("").split()))

k,n,w = inp[0],inp[1],inp[2]
total = (k*(w*(w+1)))/2
borr = (total - n)
if borr <= 0:
    print("0")
else:
    print(int(borr))