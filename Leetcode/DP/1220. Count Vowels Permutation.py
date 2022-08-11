def countVowelPermutation(self, n: int) -> int:
    #classic memo dp with options at every point 
    mod = pow(10,9) + 7
    res = {}
    for s in "aeiou":
        res[s] = 1 
        
    for i in range(n-1):
        temp = {}
        for s in "aeiou":
            if s == "a":
                temp[s] = res["e"]
            elif s == "e":
                temp[s] = (res["a"] + res["i"])%mod
            elif s == "i":
                temp[s] = (res["a"] + res["e"] + res["o"] + res["u"])%mod
            elif s == "o":
                temp[s] = (res["i"] + res["u"])%mod
            else:
                temp[s] = res["a"]
        res = temp 
        
    total = 0
    for key in res:
        total += res[key]
    return total % mod