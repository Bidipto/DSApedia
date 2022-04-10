#naive approach
def rotate( arr, n):
    arr.insert(0,arr.pop())

#more interview like approach
def rotate1( arr, n):
    temp = arr[-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp
    print(arr)

rotate1([1,2,3,4,5], 5)