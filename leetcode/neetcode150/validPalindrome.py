class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]

"""

the above algorithm works perfectly but can be optimized

t(c) = O(n)
s(c) = O(n)

"""

## optimized solution we use two pointers


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r and  not s[l].isalnum():
            l += 1
        
        while r > l and not s[r].isalnum():
            r -= 1

        if s[l].lower()  != s[r].lower():
            return False

    return True