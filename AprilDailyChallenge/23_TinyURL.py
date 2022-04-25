# good to know the approach 
# kafi sahi logic 
# we can dynamically set the length of the word according to the amount of url traffic 
# id number of url traffic is less than the 50% of the capacity increase the lenght by 1
class Codec:
    def __init__(self):
        self.dic = {}
        self.lst = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    def encode(self, longUrl: str) -> str:
        code = "".join(random.choice(self.lst) for i in range(6))
        while code in self.dic:
            code = "".join(random.choice(self.lst) for i in range(6))
        self.dic[code] = longUrl
        return "http://tinyurl.com/" + code

    def decode(self, shortUrl: str) -> str:
        return self.dic[shortUrl.split("/")[-1]]
        