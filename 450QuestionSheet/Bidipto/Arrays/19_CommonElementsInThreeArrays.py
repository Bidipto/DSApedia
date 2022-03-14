#when all the elements are same we increment all the counters
#else we increment only the counter of the least value element
#also we have to return unique common elements only
def commonElements (self,A, B, C, n1, n2, n3):
    count = []
    i = 0
    j = 0
    k = 0
    while i<n1 and j<n2 and k<n3:
        num1 = A[i]
        num2 = B[j]
        num3 = C[k]
        if num1 == num2 == num3:
            if count:
                if num1 != count[-1]:
                    count.append(num1)
            else:
                count.append(num1)
            i += 1
            j += 1
            k += 1
        else:
            if num1<=num2 and num1<=num3:
                i += 1
            elif num2<=num1 and num2<=num3:
                j += 1
            else:
                k += 1
    return count