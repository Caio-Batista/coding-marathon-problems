def bon_appetit(bill,k,b):
    total_partial = 0
    for i in range(len(bill)):
        if i != k:
            total_partial += bill[i]
    total_partial /= 2

    change = b - total_partial
    if not change:
        return 'Bon Appetit'
    else: 
        return change


if __name__ == '__main__':
    print(bon_appetit([3,10,2,9], 1, 7))