class Trienode:
    def __init__(self):
        self.children ={}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Trienode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trienode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs( i+1, child):
                            return True
                    return False
                
                else:
                    if not c in cur.children:
                        return False
                    cur = cur.children[c]
                
            return cur.isEnd

        return dfs(0, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)