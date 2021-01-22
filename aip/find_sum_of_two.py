def find_sum_of_two(A, val):
    found = set()
    while A:
        num = A.pop()
        if val - num in found:
            return True
        found.add(num)
    
    return False

if __name__ == "__main__":
    print(find_sum_of_two([2, 1, 8, 4, 7, 3], 7))
