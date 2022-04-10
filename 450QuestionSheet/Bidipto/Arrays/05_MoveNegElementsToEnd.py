# O(n2) solution but doesnt need extra space
def segregateElements(arr, n):
    first = 0
    while first<n:
        #when first we just go front 
        if arr[first] >= 0:
            first += 1
        #when we reach negative we seach for the next positice to rotate the array 
        else:
            temp = first + 1
            while temp<n and arr[temp] < 0 :
                temp += 1
            #break if temp reaches ie there is no positice number
            if temp == n:
                break
            #now temp points to a positive which needs to goto first place
            posnum = arr[temp]
            for i in range(temp,first,-1):
                arr[i] = arr[i-1]
            arr[first] = posnum
    print(arr)

segregateElements([-5, 7, -3, -4, 9, 10, -1, 11], 8)