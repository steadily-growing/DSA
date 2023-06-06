class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers ={
            "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000
        }
        res = 0

        for i in range(len(s)):
            if i+1 < len(s) and roman_numbers[s[i]] < roman_numbers[s[i+1]]:
                res -= roman_numbers[s[i]]
            else:
                res += roman_numbers[s[i]]
        return res
        