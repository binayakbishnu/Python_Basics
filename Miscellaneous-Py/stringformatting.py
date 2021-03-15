def print_formatted(number):
    l = len("{:b}".format(n))
    for i in range(1, n+1):
        print("{0:{l}d} {0:{l}o} {0:{l}X} {0:{l}b}".format(i, l=l))
        # print("{0:10d} {0:10o} {0:10X} {0:10b}".format(i, l=l))


n = int(input("Enter number: "))
print_formatted(n)

