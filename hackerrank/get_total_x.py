def get_total_x(a,b):
    
    def check_up(k, arr):
        for e in arr:
            if e % k != 0:
                return False
        return True
    
    def check_down(k, arr):
        for e in arr:
            if k % e != 0:
                return False
        return True

    divs = []

    for i in range(a[-1], b[0] + 1): 
        print(i)
        if i % a[-1] == 0 and b[0] % i == 0:
            if check_up(i, b) and check_down(i, a):
                divs.append(i)
    
    

    return len(divs)

if __name__ == '__main__':
    print(get_total_x([2,4],[16,32,96]))