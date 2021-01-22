import copy

def score_percentage(A):
    n = len(A)
    current = 0
    for e in A:
        current += e[0]/e[1]
    return current/n

def best(A1, A2):
    choice = A1
    if score_percentage(A2) >= score_percentage(A1):
        choice = A2
    return choice
    
def five_star_seller(ratings, threshold, steps=[], index=0):
    index = 0

    if score_percentage(ratings) * 100 > threshold: 
        print(score_percentage(ratings))
        return len(steps)


    def mount(current_ratings, index=0):
        if index == len(current_ratings) - 1:
            copy2 = copy.deepcopy(current_ratings)
            copy2[index][0] += 1
            copy2[index][1] += 1
            return copy2
        
        copy_a = copy.deepcopy(current_ratings)
        copy_a[index][0] += 1
        copy_a[index][1] += 1
        best_rating = best(copy_a, mount(current_ratings, index + 1))
        return best_rating

    steps.append(mount(ratings, index))
    return five_star_seller(mount(ratings, index), threshold, steps, index+1)
   


if __name__ == "__main__":
    print(five_star_seller([[4,4], [1,2], [3, 6]], 77))