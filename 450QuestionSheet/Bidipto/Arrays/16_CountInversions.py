aee = [2, 3, 5, 2, 2]

#mergesort while counting the number of insersions while mergeing the array 
#kafi important question check for review

def inversionCount(arr, n):
    temp_arr = [0]*n
    return mergesort(arr, temp_arr, 0, n-1)

def mergesort(arr, temp_arr, left, right):
    count = 0
    if left<right:
        mid = left + (right - left)//2
        
        count += mergesort(arr, temp_arr, left, mid)
        count += mergesort(arr, temp_arr, mid + 1, right)
        
        count += merge(arr, temp_arr, left, mid, right)
        
    return count

def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    count = 0
    
    while i<= mid and j <= right:
        if arr[i]<= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            k += 1
            j += 1
            count += (mid - i + 1)
    
    while i<=mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
        
    while j<=right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
        
    for i in range(left, right + 1):
        arr[i] = temp_arr[i] 
        
    return count     

print(inversionCount(aee, len(aee)))