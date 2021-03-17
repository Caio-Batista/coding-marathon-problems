def kangaroo(x1, v1, x2, v2):
    if v2 >= v1: 
        return 'NO'

    pos_fast,pos_slow = x1,x2
    while pos_fast < pos_slow:

        pos_fast += v1
        pos_slow += v2
    if pos_slow == pos_fast:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    print(kangaroo(0,3,4,2))
