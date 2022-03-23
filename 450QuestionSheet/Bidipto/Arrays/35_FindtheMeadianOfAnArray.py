import math
def find_median(self, arr):
	arr.sort()
	N = len(arr)
	if N%2:
		return arr[N//2]
	else:
		return math.floor((arr[N//2] + arr[(N//2)-1])/2)
