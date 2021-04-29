# include 1 and last digit (min(b)+1)

def getTotalX(a, b):
    c=0
    # Write your code here
    for i in range(1,min(b)+1):
        flag=0
        for j in a:
            if i%j != 0:
                flag=1
        if flag==1:
            continue
        for j in b:
            if j%i !=0:
                flag=1
        if flag==0:
            c+=1
    
    return c

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(str(total) + '\n')
