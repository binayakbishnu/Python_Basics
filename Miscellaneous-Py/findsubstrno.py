def count_substring(string, sub_string):
    count = 0
    for x in range(len(string)):
        if string[x:].startswith(sub_string):
            # checks if part of the string starts with substring
            # equivalent to checking if the string contains substring
            count += 1
    return count


if __name__ == '__main__':
    string = input("Enter string: ").strip()
    sub_string = input("Enter sub_string: ").strip()

    count = count_substring(string, sub_string)
    print(count)

'''Sample:
String: ABCDCDC
Sub_string: CDC
Output: 2

AB (CDC) DC
ABCD (CDC)
'''
