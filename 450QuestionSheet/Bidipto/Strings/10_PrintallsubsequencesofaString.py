S = "abcd"

def subsequences(S):
    def magic(res,i):
        if i == len(S):
            if len(res)>0:
                print(res)
            return

        #take
        magic(res+S[i],i+1)

        #nottake
        magic(res,i+1)
    
    magic("",0)

subsequences(S)