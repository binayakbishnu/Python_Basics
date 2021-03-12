def bsort_num(arr,q):
    for i in range(q-1):
        #print("i = {}".format(i))
        for j in range(q-i-1):
            #print("j = {}".format(j))
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            #print(arr)

def bsort_str(arr,q):
    for i in range(q-1):
        #print("i = {}".format(i))
        for j in range(q-i-1):
            #print("j = {}".format(j))
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            #print(arr)

numbers = [4,1,8,7,2,10,0]
bsort_num(numbers,7)
print("Final list:")
print(numbers)

strings = ["Binayak","Bishnu","Vellore","Institute"]
bsort_str(strings,4)
print("Final list:")
print(strings)

