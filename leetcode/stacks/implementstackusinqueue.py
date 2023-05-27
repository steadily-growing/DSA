class MyStack:

    def __init__(self):
        self.myKew = deque()

    def push(self, x: int) -> None:
        self.myKew.append(x)

    def pop(self) -> int:
        for i in range (len(self.myKew)-1):
            self.push(self.myKew.popleft())
        return self.myKew.popleft()

    def top(self) -> int:
        return self.myKew[-1]

    def empty(self) -> bool:
        return len(self.myKew) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()