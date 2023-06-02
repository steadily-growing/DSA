class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        result = 0

        while x:
            ones_place = int(math.fmod(x, 10))
            x = int(x/10)

            if (result > MAX//10 or (result == MAX//10 and ones_place >= MAX%10)):
                return 0
            if (result < MIN//10 or (result == MIN//10 and ones_place <= MIN%10)):
                return 0
            result = (result * 10) + ones_place
        return result

        