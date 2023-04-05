class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        l = 0
        r = len(x_str)-1
        while l <= r:
            x_list = list(x_str)
            x_list[l] ,x_list[r] = x_list[r], x_list[l]
            reversed_x_str = "".join(x_list)

            if x_str == reversed_x_str:
                l +=1
                r -=1
            else:
                return False
        return True
     
