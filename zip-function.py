list1 = [1,2,3]
list2 = ['A','B','C']

tuple1 = (11,12,13)
tuple2 = ('L','M','N')

zip1 = zip(list1)
zip2 = zip(list1,list2)
zip3 = zip(tuple1)
zip4 = zip(tuple1,tuple2)
zip5 = zip(list1,tuple1)
zip5 = zip(list1,tuple2)

# print(zip1)
# print(zip2)
# print(zip3)
# print(zip4)
# print(zip5)

ziplist1 = list(zip1)
ziplist2 = list(zip2)
ziplist3 = list(zip3)
ziplist4 = list(zip4)
ziplist5 = list(zip5)

print(ziplist1)
print(ziplist2)
print(ziplist3)
print(ziplist4)
print(ziplist5)
print()

#Unzipping
A, B = zip(*ziplist4)
print(A)
print(B)
print()

# print(zip(*ziplist4))