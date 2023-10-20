class OrderedStream:

    def __init__(self, n: int):
        self.lst = [None]*n
        self.pointer = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.lst[idKey-1] = value

        res = []

        while self.pointer < len(self.lst) and self.lst[self.pointer] is not None:
            res.append(self.lst[self.pointer])
            self.pointer +=1
        return res
    
            



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)