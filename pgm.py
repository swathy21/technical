s,b=list(map(int,input().split()))
s = s ^ b
b = s ^ b
s = s ^ b
print(s,b)
    
