def divisible_sum_pairs(n, k, ar):
    ans = 0
    sums = {}
    while ar:
        num = ar.pop()
        for e in ar:
            if sums.get(str(e+num)) is not None:
                sums[str(e+num)] += 1
            else:
                sums[str(e+num)] = 1
    for key in sums.keys():
        if int(key) % k == 0:
            ans += sums[key] 
    return ans



if __name__ == '__main__':
    print(divisible_sum_pairs(6,3,[1, 3, 2, 6, 1, 2]))