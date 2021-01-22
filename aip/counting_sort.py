def counting_sort(A):
    aux = [0] * 100000
    ordered = []
    for e in A:
        aux[e] += 1
    for i in range(len(aux)):
        if aux[i] > 0:
            for _ in range(aux[i]):
                ordered.append(i)

    return ordered