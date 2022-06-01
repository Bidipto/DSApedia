#here we use the concept of repeated division
#since the number is very large we cant do repeated division 
#if the divendend is greater that the square of the number 
#we remove the square of the number and add the divisor of the to the quotient
#we we have removed divisor time divisor ie square of the divisor
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = (dividend>0) == (divisor>0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            div = divisor
            temp = 1
            while dividend >= div:
                dividend -= div
                res += temp
                temp = temp<<1
                div = div<<1
        if not neg:
            res = -res
            
        return min( 2147483647, max(res,-2147483648)) 