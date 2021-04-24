numbers = input().split()

n = int(numbers[0])
m = int(numbers[1])

def isPrime(x):
    for i in range(2,(x//2) + 1):
        if x%i==0:
            return 0
            
    return 1
    
flag=1

if isPrime(m) == 1: #checking if m prime
    for i in range(n+1,m): #checking if any other prime within n,m
        if isPrime(i) == 1:
            print("NO")
            exit(0)
else:
    print("NO")
    exit(0)

print("YES")
