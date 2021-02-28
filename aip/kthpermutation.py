
def get_permutation(A, k):
    def factorial(n):
        number = 1
        for i in range(n, 1, -1):
            number *= i
        return number

    arr=[i for i in range(1,len(A)+1)]
    ans=""
    while(arr):
        index=k // (factorial(len(arr)-1)) 

        if k % (factorial(len(arr)-1)) == 0:
            index-=1
        ans+=str(arr[index])

        k = k - (factorial(len(arr)-1)) * index

        arr.remove(arr[index]) 
    return(ans)

if __name__ == "__main__":
    for i in range(1, 362881):
        print(get_permutation("123456789", i))