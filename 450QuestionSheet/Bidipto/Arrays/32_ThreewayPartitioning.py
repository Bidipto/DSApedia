#similar to 012 sort or sortcolours in leetcode
def threeWayPartition(self, arr, a, b):
    one = 0
    two = 0
    three = len(arr)-1
    while two<=three:
        if arr[two] < a:
            arr[two], arr[one] = arr[one], arr[two]
            two += 1
            one += 1
        elif arr[two] >= a and arr[two] <= b:
            two += 1
        else:
            arr[two], arr[three] = arr[three], arr[two]
            three -= 1
