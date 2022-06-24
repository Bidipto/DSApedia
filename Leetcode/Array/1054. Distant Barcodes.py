# 1054. Distant Barcodes

def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        #odd even indexes technique 
        #most_commmon returns list of tuples 
        counter = Counter(barcodes)
        N = len(barcodes)
        res = [0] * N
        
        arr = counter.most_common()
        arr = [list(lst) for lst in arr]
        # print(arr)
        j = 0
        for i in range(0,N,2):
            if arr[j][1]>0:
                res[i] = arr[j][0]
                arr[j][1] -= 1
            else:
                j += 1
                res[i] = arr[j][0]
                arr[j][1] -= 1
        for i in range(1,N,2):
            if arr[j][1]>0:
                res[i] = arr[j][0]
                arr[j][1] -= 1
            else:
                j += 1
                res[i] = arr[j][0]
                arr[j][1] -= 1
        
        return res