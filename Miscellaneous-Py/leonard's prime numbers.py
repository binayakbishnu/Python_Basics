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
