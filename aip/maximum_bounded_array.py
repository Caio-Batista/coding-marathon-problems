def maximum_bounded_array(array_size, lowBound, upBound):
    if array_size > (upBound - lowBound) * 2:
        return None
    
    def best(arr1, arr2):
        if not arr1: return arr2
        if not arr2: return arr1

        if arr1[0] > arr2[0]:
            return arr1
        else:
            return arr2
    
    def mount(start):
        if start == upBound:
            return []

        array = []
        for i in range(start, upBound + 1):
            array.append(i)
        for j in range(upBound - 1, lowBound - (upBound - lowBound), -1):
            if len(array) == array_size:
                break
            else:
                array.append(j)
        
        return best(array, mount(start+1))

    return mount(lowBound)

if __name__ == "__main__":
    print(maximum_bounded_array(4, 10, 12))
    print(maximum_bounded_array(6, 1, 3))
    print(maximum_bounded_array(5, 9, 13))