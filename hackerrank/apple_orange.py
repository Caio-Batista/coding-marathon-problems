def apple_orange(s, t, a, b, apples, oranges):
    def isInRange(s,t,k):
        if s<=k<=t:
            return True
        else:
            return False
    apples_amount = 0
    oranges_amount = 0

    for apple in apples:
        if  isInRange(s,t,apple + a):
            apples_amount += 1
    for orange in oranges:
        if  isInRange(s,t,orange + b):
            oranges_amount += 1
    return [apples_amount, oranges_amount]

if __name__ == '__main__':
    print(apple_orange(7, 11, 5, 15,[-2, 2, 1],[5, -6]))
