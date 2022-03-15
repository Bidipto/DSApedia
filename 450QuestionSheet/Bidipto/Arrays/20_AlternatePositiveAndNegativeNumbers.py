Arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
arr = [-1, -2, -3, 4, 5, 6]


#solution without using extra space but sadly its gives TLE, ahha 
#solutin using extra space would run tho wtf
def rearrange(arr, n):
    #if flag is true we need a postiive number for the index
    #else if flag is flase we need a negative number for the index
    #observation 0 is cosidered pos, makes life easier
    flag = True
    index = 0
    for i in range(n):
        val = arr[i]
        # print(index, i, flag, val)
        if flag:
            if val>= 0:
                #if the positive number is present in the index itself we do nothing
                if i == index:
                    flag = not flag
                    index += 1
                #if pos and we need a pos it a index earlier we just rotate
                #and since index is not equal to i its for sure we have seen negative numbers which is required in the next pos
                #therefore we just rotate and increment the index by 2 and keep the flag as it is
                else:
                    arr[index+1:i+1] = arr[index:i]
                    arr[index] = val
                    index += 2
        else:
            if val<0:
                #if the negative number is present in the index itself we do nothing
                if i == index:
                    flag = not flag
                    index += 1
                #if neg and we need a pos it a index earlier we just rotate
                else:
                    arr[index+1:i+1] = arr[index:i]
                    arr[index] = val
                    index += 2
    return arr

print(rearrange(arr, len(arr)))