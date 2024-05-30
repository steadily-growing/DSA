class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i , j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1 #we increment the i after we find it in the string t
            j+=1   
        return i == len(s)



