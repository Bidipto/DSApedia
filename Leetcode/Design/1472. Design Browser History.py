# 1472. Design Browser History

class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = []
        self.stack.append(homepage)
        self.pointer = 0

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.pointer + 1]
        self.stack.append(url)
        self.pointer += 1

    def back(self, steps: int) -> str:
        self.pointer = max(0,self.pointer-steps)
        return self.stack[self.pointer]
    
    def forward(self, steps: int) -> str:
        self.pointer = min(self.pointer + steps, len(self.stack)-1)    
        return self.stack[self.pointer]
