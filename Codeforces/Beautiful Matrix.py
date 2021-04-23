L=[]

for _ in range(5):
    R = input().split()
    R = [int(i) for i in R]
    L.append(R)
#print(L)  
i=0
j=0

for i in range(5):
    for j in range(5):
        if L[i][j] == 1:
            x = i
            y = j

s = (abs(x-2) + abs(y-2))

print(s)
