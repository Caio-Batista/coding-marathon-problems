def counting_valleys(path):
    valleys = 0
    is_above_sea = True
    ref = 0
    for e in path:
        if e == 'U':
            if not is_above_sea and ref == -1:
                is_above_sea = True
            ref += 1
        else:
            if is_above_sea and ref == 0:
                is_above_sea = False
                valleys += 1
            ref -= 1

    return valleys


if __name__ == '__main__':
    print(counting_valleys('UDDDUDUU'))