def power(num, exp):
    result = 1
    if exp >= 0:
        for _ in range(exp):
            result *= num
    else:
        for _ in range(-exp):
            result *= num
        result = 1 / result
    return result

def main():
    try:
        num = float(input('Enter number: '))
    except ValueError:
        print("Invalid number input")
        exit()

    try:
        exp = int(input('Enter exponent: '))
    except ValueError:
        print("Invalid exponent input")
        exit()

    result = power(num, exp)

    print("Result:", result)

if __name__ == "__main__":
    main()
