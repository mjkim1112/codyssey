def main():
    # selection sort algorithm
    seq = list(map(float, input("숫자 입력: ").split()))
    n = len(seq)
    
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if seq[j] < seq[least]:
                least = j
        seq[i], seq[least] = seq[least], seq[i]  # swap
    
    print("정렬 결과:", seq)

if __name__ == "__main__":
    main()