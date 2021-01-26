def breaking_records(scores):
    max_num,max_amount = scores[0],0
    min_num,min_amount = scores[0],0

    for e in scores:
        if e < min_num:
            min_amount += 1
            min_num = e
        elif e > max_num:
            max_amount += 1
            max_num = e
    return [max_amount, min_amount]

if __name__ == '__main__':
    print(breaking_records([10, 5, 20, 20, 4, 5, 2, 25, 1]))
    print(breaking_records([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))