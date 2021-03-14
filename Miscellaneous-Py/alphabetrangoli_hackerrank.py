def print_rangoli(size):
    # your code goes here
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters = "".join([i.lower() for i in letters])
    # print(letters)
    if size==1:
        print("a")
        return 0

    rawpattern = []
    for j in range(size-1, -1, -1):
        row = "-".join(letters[j:size])
        rawpattern.append((row[::-1] + "-" + row[2::]).center(4*size-3, '-'))

    print("\n".join(rawpattern+rawpattern[len(rawpattern)-2::-1]))


n = int(input("Enter size: "))
print_rangoli(n)
