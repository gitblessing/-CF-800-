a,b = map(int,input().split())
days = (min(a,b), (max(a,b)-min(a,b)) //2) 
print(*days,sep=" ")
