def check(A, first, last):
    for i in range(first, last - 1):
        if A[i+1] - A[i] != A[i+2] - A[i+1]:
            return False
    return True

def solution(A):
    res_array={}
    def try_velocity(A, last_index, index=0, temp={}):
        if index == len(A) - 2 or (last_index == len(A) - 1):
            if not check(A,index,last_index):
                return []
            temp[f'{[index,last_index]}'] = [index,last_index]
            return [index,last_index]
 
        if check(A,index,last_index):
            temp[f'{[index,last_index]}'] = [index,last_index]
            return [try_velocity(A, last_index+1, index,temp) + try_velocity(A, index+3, index+1, temp)]
        
        return try_velocity(A, index+3, index+1, temp)
    
    try_velocity(A,2,0,res_array)
    return len(res_array.keys())



if __name__ == "__main__":
    print(solution([-1,1,3,3,3,2,3,2,1,0,4,4,4,4,4,4,3,2,1,0,1,1,1,1,1,4,2,2,6,1,4]))
