n,m = map(int,input().split())
chest = list(map(int,input().split()))
key = list(map(int,input().split()))

ch_o = [ x for x in chest if x%2==0]
ch_e = [ x for x in chest if x%2!=0] 
ky_o = [ x for x in key if x%2==0]
ky_e = [ x for x in key if x%2!=0]

print(min(len(ky_e),len(ch_o)) + min(len(ch_e),len(ky_o)))

