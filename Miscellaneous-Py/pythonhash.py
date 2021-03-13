integers = input("Enter numbers separated by spaces: ").split()
# takes input, converts to string list
print(integers)

integers = [int(x) for x in integers]
print(integers)

tu = tuple(integers)
print(tu)

print(hash(tu))
