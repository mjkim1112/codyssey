try:
    num = int(input('Enter number: '))
except ValueError:
    print("Invalid number input")
    exit()

try:
    exp = int(input('Enter exponent: '))
except ValueError:
    print("Invalid exponent input")
    exit()

result = 1
for i in range(exp):
    result *= num

print("Result:", result)


