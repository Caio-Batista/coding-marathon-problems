def binary_search(A, start, end, k):
    if end >= start:
        mid = (end + start) // 2
        if A[mid] == k:
            return True
        elif A[mid] < k:
            return binary_search(A, mid + 1, end, k)
        else:
            return binary_search(A, start, mid - 1, k)
    else:    
        return False

if __name__ == "__main__":
    print(binary_search([1,2,3,4,5,6,33,44,45],0,8,34))