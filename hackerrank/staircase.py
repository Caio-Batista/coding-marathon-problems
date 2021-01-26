def staircase(n):
    staircase_ans = []
    last_line = ['#' for j in range(n)]
    for i in range(1, n):
        temp = [' '] * (n-i)
        temp2 = ['#'] * i 
        staircase_ans.append(temp + temp2)

    staircase_ans.append(last_line)
    for e in staircase_ans:
        print(''.join(e), end='\n')
if __name__ == '__main__':
    staircase(6)
