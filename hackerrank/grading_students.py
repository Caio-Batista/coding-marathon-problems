def grading_students(arr):
    new_grades = []
    for e in arr:
        if e <= 37:
            new_grades.append(str(e))
        elif e % 10 == 3 or e % 10 == 4:
            new_grades.append(str((e//10) * 10 + 5))
        elif e % 10 == 8 or e % 10 == 9:
            new_grades.append(str((e//10) * 10 + 10))  
        else:
            new_grades.append(str(e))
    for k in new_grades:
        print(k, end='\n')



if __name__ == '__main__':
    arr = [73, 67, 38, 33]
    grading_students(arr)
