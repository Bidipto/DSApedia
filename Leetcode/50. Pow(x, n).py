# 50. Pow(x, n)
#pretty basic and algorithmn to get the pow of a number
#shanti se sochne se intuitive be
#needs review on the different approaches to this problem
def myPow(self, x: float, n: int) -> float:
    if n == 0:
        return 1
    if n<0:
        return 1/self.myPow(x,-n)
    if not n%2:
        return self.myPow(x*x,n/2)
    
    return x*self.myPow(x,n-1)
        