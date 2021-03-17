def school_jump(n):
    steps = [5,4,3,2,1]
    
    path = []
    current_sum = 0  
    for e in steps:
        while current_sum < n:
            current_sum += e
            path.append(e)
        if current_sum > n:
            current_sum -= e
            path.pop()
        elif current_sum == n:
            break


    return len(path)

print(school_jump(15))
print(school_jump(16))