# 2296. Design a Text Editor
# two stack approach 
class TextEditor:

    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        for i in text:
            self.left.append(i)

    def deleteText(self, k: int) -> int:
        res = 0
        while self.left and k:
            k -= 1
            self.left.pop()
            res += 1
        return res

    def cursorLeft(self, k: int) -> str:
        # print(self.left,self.right,k)   
        while k and self.left:
            self.right.append(self.left.pop())
            k -= 1
        # print(self.left,self.right)  
        return "".join(self.left[max(0,len(self.left)-10):])
        

    def cursorRight(self, k: int) -> str:
        # print(self.left,self.right,k)   
        while k and self.right:
            self.left.append(self.right.pop())
            k -= 1
        # print(self.left,self.right)   
        return "".join(self.left[max(0,len(self.left)-10):])