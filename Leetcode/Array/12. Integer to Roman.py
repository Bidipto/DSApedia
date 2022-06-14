# 12. Integer to Roman
def intToRoman(self, num: int) -> str:
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    roman = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    
    res = ""
    
    for i,val in enumerate(values):
        res += (num//val)*roman[i]
        num %= val
        
    return res