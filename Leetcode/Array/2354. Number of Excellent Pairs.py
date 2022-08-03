def countExcellentPairs(self, arr: List[int], k: int) -> int:
    #inclusion-exclution principal 
    #bits(num1 or num2) + bits(num1 and num2) = bits(num1) + bits(num2)
    #.bit_count() returns the number of bits
    
    c = collections.Counter([bin(x).count("1") for x in set(arr)])
    res = 0
    
    for val1 in c:
        for val2 in c:
            if val1 + val2>=k:
                res += (c[val1]*c[val2])
    
    return res