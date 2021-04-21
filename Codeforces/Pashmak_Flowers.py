number = int(input())

L = input().split()
L = [int(i) for i in L]

x = max(L) - min(L)
L1 = L
L1.sort()
m = abs(L1[number-1]- L1[number-2])

c=-1

for i in range(number-1):
    for j in range(i+1,number):
        if m<abs(L[i]-L[j]):
            m = abs(L[i]-L[j])
            c=1
        elif m == abs(L[i] - L[j]):
            c+=1
            
print(x,c)
