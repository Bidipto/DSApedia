#a kinda light questions after KLP algo 
def printSequence(self,S):
    str = ["2", "22", "222",
    "3", "33", "333",
    "4", "44", "444",
    "5", "55", "555",
    "6", "66", "666",
    "7", "77", "777", "7777",
    "8", "88", "888",
    "9", "99", "999", "9999" ]
    res = ""
    for i in S:
        if i == " ":
            res += "0"
        else:
            res += str[ord(i)-ord("A")]
        
    return res