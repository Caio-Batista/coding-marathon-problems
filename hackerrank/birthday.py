def birthday(s, d, m):
    ans = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            ans +=1
    return ans

if __name__ == '__main__':
    print(birthday([4],4,1))
    print(birthday([1, 2, 1, 3, 2],3,2))