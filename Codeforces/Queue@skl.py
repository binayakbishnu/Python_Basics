inp = input().split()
n = int(inp[0])
t = int(inp[1])
queue = input()

c = 0
L = [q for q in queue]


for times in range(0,t):
    i=0
    while(i<len(L)-1):
        c+=1
        if L[i] == 'B' and L[i+1] == 'G':
            L[i],L[i+1] = L[i+1],L[i]
            i+=2
        else:
            i+=1
    
print("".join(L))
