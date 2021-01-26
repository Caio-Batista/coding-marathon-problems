def miniMaxSum(arr):
    ordered = count_sort(arr)
    min_sum = sum(ordered[0:4])
    max_sum = sum(ordered[1:])
    print(f'{min_sum} {max_sum}')

def count_sort(arr):
    temp = [0] * 100000
    ordered = []
    
    for e in arr:
        temp[e] += 1
    for i in range(len(temp)):
        for _ in range(temp[i]):
            ordered.append(i)
    print(ordered)
    return ordered

if __name__ == '__main__':
    arr = [7, 69, 2, 221, 8974]
    miniMaxSum(arr)