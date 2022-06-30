# 394. Decode String

def decodeString(self, s: str) -> str:
    #decoding using recursive calls
    def magic(s):
        temp = ""
        i = 0
        N = len(s)
        while i<N:
            multiplier = 0
            if "1"<=s[i]<="9":
                #need for a multiplier and second while for numebers more then 9
                while "0"<=s[i]<="9":
                    multiplier *= 10
                    multiplier += int(s[i])
                    i += 1
                #start denote the index jisse recursive call meh jayega
                #num is the number of brackets 
                i += 1
                start = i
                num = 1
                #loop to serach when the current breacket ends
                while num != 0:
                    if s[i] == "[":
                        num += 1
                    elif s[i] == "]": 
                        num-= 1
                    i += 1
                        
                temp += (multiplier * magic(s[start:i-1]))
            
            else:
                #if there is not multiplier we just add to the return string
                temp += s[i]
                i += 1
        
        # print(s, temp)
        return temp
    
    return magic(s)