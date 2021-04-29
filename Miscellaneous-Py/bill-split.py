def bonAppetit(bill, k, b):
  
    s=0
    for i in range(len(bill)):
        if i!=k:
            s+=bill[i]
    # print(s)
    
    s = s//2
    
    if s==b:
        print("Bon Appetit")
    else:
        print(b-s)
        
        
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())

bonAppetit(bill, k, b)
