class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_character = {}

        for char in s:
            if char not in unique_character:
                unique_character[char] = 1
            else:
                unique_character[char] += 1

        for i in range(len(s)):
            if unique_character[s[i]] == 1:
                return i
        return -1
        

          

        

