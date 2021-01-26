def migratory_birds(arr):
    ans = float('Inf')
    aux = {} 
    for e in arr:
        if aux.get(str(e)) is not None:
            aux[str(e)] += 1
        else:
            aux[str(e)] = 1
    
    maximum = 0
    for key, value in aux.items():
        if value > maximum:
            maximum = value
            ans = int(key)
        elif value == maximum and int(key) < ans:
            ans = int(key)
    return ans


if __name__ == '__main__':
    print(migratory_birds([1,5,5,5,4,4,4,3]))