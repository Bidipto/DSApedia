class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.dic = collections.defaultdict(list)
        self.maxFreq = 0
        

    def push(self, val: int) -> None:
        #increase the frequency of the element 
        self.freq[val] += 1
        currFreq = self.freq[val]
        #append the element in that freq stack
        self.dic[currFreq].append(val)
        #check if this is the maxfreq
        self.maxFreq = max(self.maxFreq,currFreq)

    def pop(self) -> int:
        #pop the last element with maxfreq and 
        #then decrease the freq of the elementby 1
        #if there doesnt exist any element with the max freq
        #and also its gurateed thath there will be atleast one element
        ele = self.dic[self.maxFreq].pop()
        self.freq[ele] -= 1
        if not self.dic[self.maxFreq]:
            self.maxFreq -= 1
        return ele