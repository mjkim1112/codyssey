def main():
    try:
        seq = list(map(float, input("숫자 입력: ").split()))
    except ValueError:
        print("Invalid Input")
        exit()
    if not seq:
        print("none")
        return
        
    min = seq[0]
    max = seq[0]
    
    for num in seq[1:]:
        if num < min:
            min= num
        if num > max:
            max = num

    print("Min:", min, "Max:", max)

if __name__ == "__main__":
    main()
