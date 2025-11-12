"""
use 2 stacks, one for backward pages, one for forward pages, and keep track of current
alternative approach: linkedlist but more memory
"""
class BrowserHistory:

    def __init__(self, homepage: str):
        self.forward_hist = []
        self.back_hist = []
        self.current = homepage

    def visit(self, url: str) -> None:
        self.back_hist.append(self.current)
        self.forward_hist = []
        self.current = url
        

    def back(self, steps: int) -> str:
        t = ""
        while steps > 0 and self.back_hist:
            t = self.back_hist.pop()
            self.forward_hist.append(self.current)
            self.current = t
            steps -= 1
        return self.current
        

    def forward(self, steps: int) -> str:
        t = ""
        while steps > 0 and self.forward_hist:
            t = self.forward_hist.pop()
            self.back_hist.append(self.current)
            self.current = t
            steps -= 1
        return self.current
            
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)