code = input()

L=[]

i=0
while(i<len(code)):
    if code[i] == '.':
        L.append(0)
        i+=1
    elif i==len(code)-1:
        break
    elif code[i] == '-' and code[i+1] == '.':
        L.append(1)
        i+=2
    elif code[i] == '-' and code[i+1]== '-':
        L.append(2)
        i+=2
        
L = [str(i) for i in L] #converting elements to string type

print("".join(L))
