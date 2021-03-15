def solve(s):
    s2=""
    for i in range(len(s)):
        if i==0:
            s2+=s[i].upper()
        elif s[i-1]==" ":
            s2+=s[i].upper()
        else:
            s2+=s[i]
    s=s2
    return s

s = input("Enter string: ")

result = solve(s)

print(result)
