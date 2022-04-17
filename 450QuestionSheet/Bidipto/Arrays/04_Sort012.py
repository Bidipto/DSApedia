#good logic but the algo is unstable
#the relative order of the elements is not preserved

def sort012(self,arr,N):
    one = 0
    two = 0
    three = N-1
    while two<=three:
        if arr[two] == 0:
            arr[two], arr[one] = arr[one], arr[two]
            two += 1
            one += 1
        elif arr[two] == 1:
            two += 1
        else:
            arr[two], arr[three] = arr[three], arr[two]
            three -= 1