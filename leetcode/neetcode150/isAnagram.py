class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countT ,countS = {},{}

        if len(s) != len(t):
            return False


        for c in range(len(s)):
            countT[t[c]] = 1+ countT.get(t[c], 0)
            countS[s[c]] = 1+ countS.get(s[c], 0)


        for i in countS:
            if countS[i] != countT.get(i, 0):
                return False
        return True



        