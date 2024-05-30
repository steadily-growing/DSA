class RandomizedSet:

    def __init__(self):
        self.map = defaultdict(int)
        self.lst = []        
        self.len = 0

    def insert(self, val: int) -> bool:
        if val in self.map: return False

        self.lst.append(val)
        self.map[val] = self.len
        self.len +=1

        return True


    def remove(self, val: int) -> bool:
        if val not in self.map: return False
        val_ind = self.map[val]
        last_element = self.lst[-1]

        #this part cares about the elements new position in the map and in the lsit
        self.lst[val_ind], self.map[last_element] = last_element, val_ind

        self.lst.pop()
        del self.map[val]
        self.len -=1
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()