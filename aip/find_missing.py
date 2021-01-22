def find_missing(input_1):
    soma = sum(input_1) 
    n = len(input_1) + 1 
    total_required = (n * ( n + 1 ) ) / 2

    return total_required - soma

if __name__ == "__main__":
    print(find_missing([3, 7, 1, 2, 8, 4, 5]))