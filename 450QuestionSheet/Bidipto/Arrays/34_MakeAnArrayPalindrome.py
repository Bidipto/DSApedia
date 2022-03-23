arr = [11,2,1,3,11]

def merge(arr):
    i = 0
    j = len(arr) -1
    res = 0
    while i<j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        elif arr[i] < arr[j]:
            res += 1
            arr[i+1] += arr[i]
            i += 1
        else:
            res += 1
            arr[j-1] += arr[j]
            j -= 1
    print(arr)
    print(res)

merge(arr)