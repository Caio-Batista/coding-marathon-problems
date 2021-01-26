def page_count(n,p):
    book = [(None, 1)] + [(i,i+1) for i in range(2, n+1, 2)]
    r_leaps, l_leaps = 0,0
    for i in range(len(book)):
        if book[i][0] == p or book[i][1] == p:
            break
        l_leaps += 1

    for i in range(len(book) - 1,0,-1):
        if book[i][0] == p or book[i][1] == p:
            break    
        r_leaps += 1

    return min(r_leaps, l_leaps)

if __name__ == '__main__':
    print(page_count(5,3))