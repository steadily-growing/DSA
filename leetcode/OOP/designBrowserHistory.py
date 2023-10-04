class BrowserHistory:
    """
    [1,2,3,4]

    f= [3,] b= [0,1,2]
    """

    def __init__(self, homepage: str):
        self.backStack = [homepage] 
        self.forwardStack = []
      

    def visit(self, url: str) -> None:
        self.backStack.append(url)
        self.forwardStack = []
        

    def back(self, steps: int) -> str:
        steps = min(steps, len(self.backStack) -1 )
        while steps!=0:
            self.forwardStack.append(self.backStack.pop())
            steps -=1
        return self.backStack[-1]
        

    def forward(self, steps: int) -> str:
        steps = min(steps, len(self.forwardStack) -1 )
        while steps!=0 and self.forwardStack:
            self.backStack.append(self.forwardStack.pop())
            steps -=1
        return self.backStack[-1] if self.backStack else ""

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)