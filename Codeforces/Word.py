t = input()

c1=0
c2=0

for i in t:
    if i.isupper():
        c1+=1
    elif i.islower():
        c2+=1
        
if c1>c2:
    x = [i.upper() for i in t]
    
else:
    x = [i.lower() for i in t]
    
t = "".join(x)

print(t)
