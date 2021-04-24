# take q input for number of cases
# for each q take input n
# find the maximum number of distinct prime factors a number in range
# 1 to n (inclusive) can have
# Example: for n = 500
# the maximum number of unique prime factors a number from 1 to 500 can have is 4

def primeCount(n):
    
    prime=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    c,primorial=0,1
    for j in prime:
        primorial = primorial*j
        if primorial<=n:
            c+=1
    return c
        
    
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        print(str(result) + '\n')
