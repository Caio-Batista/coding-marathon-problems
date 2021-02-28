def get_money_spent(keyboards,drives,b):
    bigger = keyboards
    smaller = drives

    if len(keyboards) < len(drives):
        bigger = drives
        smaller = keyboards

    ans = 0
    while bigger:
        m = bigger.pop()
        for i in range(len(smaller)):
            if m + smaller[i] <= b and m + smaller[i] > ans:
                ans = m + smaller[i]

    return -1 if ans == 0 else ans

if __name__ == '__main__':
    print(get_money_spent([3,1] , [5,2,8] ,10))