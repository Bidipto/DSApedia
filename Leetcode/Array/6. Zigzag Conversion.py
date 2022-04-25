# 6. Zigzag Conversion/*n=numRows
# Δ=2n-2    1                           2n-1                         4n-3
# Δ=        2                     2n-2  2n                    4n-4   4n-2
# Δ=        3               2n-3        2n+1              4n-5       .
# Δ=        .           .               .               .            .
# Δ=        .       n+2                 .           3n               .
# Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
# Δ=2n-2    n                           3n-2                         5n-4


def convert(self, s: str, N: int) -> str:
        #2 * 1...2...3

        res = ""
        arr = list(s)
        jump = N + N -2
        if N == 1:
            return s
        for i in range(N):
            for j in range(i,len(s),jump):
                res += arr[j]
                if i != 0 and i != N-1:
                    nex = j+((N-1-i)*2) #difference between a element in s straight and in the slant in same row
                    if nex< len(s):
                        res += arr[nex]
                    
        return res