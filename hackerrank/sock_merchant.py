def sock_merchant(ar):
    aux = {}
    for e in ar:
        if aux.get(str(e)) is not None:
            aux[str(e)] += 1
        else:
            aux[str(e)] = 1

    total = 0
    for value in aux.values():
        total += value // 2
    
    print(total)

if __name__ == '__main__':
    print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))