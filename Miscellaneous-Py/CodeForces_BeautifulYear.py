from collections import Counter

yr = int(input())

flag = 0
i=1

while flag==0:
    y=str(yr+i)
    i+=1
    
    freq = Counter(y)
    if(len(freq) == len(y)):
        print(y)
        flag=1
    
