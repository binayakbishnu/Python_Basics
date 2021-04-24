number = input()    #taking as string

c=0

for i in number:
    if i == '7' or i == '4':
        c+=1
        
#print(c)
        
if c== 7 or c== 4:
    print('YES')
else:
    print('NO')
