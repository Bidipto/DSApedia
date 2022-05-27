# 1109. Corporate Flight Bookings
# the idea is to prefix sum nahi toh tle ho jayega
# for [i,j] in bookings arr we add the num of passengers at i 
# and then substrat at j
def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*n
        
        for u,v,w in bookings:
            res[u-1] += w
            if v != n:
                res[v] -= w
                
        for i in range(1,n):
            res[i] += res[i-1]
        
        return res