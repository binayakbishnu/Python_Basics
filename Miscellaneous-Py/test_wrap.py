def wrap(string, max_width):
    return "\n".join(string[i:i+max_width] for i in range(0, len(string), max_width))


string = input("Enter string: ")
max_width = int(input("Enter width: "))
result = wrap(string, max_width)
print(result)
