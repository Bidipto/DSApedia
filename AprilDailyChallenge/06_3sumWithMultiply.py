#threesome with some beautiful math 

def threeSumMulti(self, arr: List[int], target: int) -> int:
    dic = Counter(arr)
    print(dic)
    arr = list(set(arr))
    arr.sort()
    res = 0
    for i in range(len(arr)):
        first = arr[i]
        for j in range(i,len(arr)):
            second = arr[j]
            num = target - first - second 
            lo = j
            hi = len(arr) - 1
            while lo<=hi:
                mid = lo + (hi-lo)//2
                third = arr[mid]
                if third == num:
                    if first != second != third: 
                        res += dic[first] * dic[second] * dic[third]
                    elif first == second != third: 
                        #(n(n-1)//2)
                        res += ((dic[first]-1) * dic[first] * dic[third]) // 2
                    elif first != second == third: 
                        #(n(n-1)//2)
                        res += (dic[first] * dic[second] * (dic[third]-1)) //2
                    else:
                        #(n(n-1)(n-2)//6)
                        res += (dic[first] * (dic[first]-1) * (dic[first]-2))//6                            
                    break
                elif third>num:
                    hi = mid - 1
                else:
                    lo = mid + 1
    return res%(pow(10,9)+7)