

def forming_magic_square(s):
    s = sum(s, [])
    magics = [
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [4, 9, 2, 3, 5, 7, 8, 1, 6]
    ]

    mincost = float('Inf')

    for magic in magics:
        current_diff = 0
        for i,j in zip(s, magic):
            current_diff += abs(j-i)
        if current_diff < mincost:
            mincost = current_diff
    return mincost



if __name__ == '__main__':
    print(forming_magic_square([[5, 3, 4], [1, 5, 8], [6, 4, 2]])) # 7
    print(forming_magic_square([[8,3,4],[1,5,9],[6,7,2]])) # 0
    print(forming_magic_square([[4, 8, 2],[4, 5, 7],[6, 1, 6]])) # 4
    print(forming_magic_square([[4, 5, 8], [2, 4, 1], [1, 9, 7]])) # 14
    #print(check_all([[8, 4, 4], [1, 5, 8], [6, 4, 2]]))
    #print(check_all([[4, 8, 2],[4, 5, 7],[6, 1, 6]]))
