import cmath

number = complex(input("Enter number: "))
# print(number)
real = number.real
imag = number.imag
# print(real,imag)

# print(cmath.polar(complex(real,imag)))
x = cmath.polar(complex(real,imag))
print(x[0])
print(x[1])

