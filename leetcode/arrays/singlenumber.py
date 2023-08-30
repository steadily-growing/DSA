#this solution uses extra space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """

        { 2:2, 1:1}

        i
        [2,2,1]

        for value, counter in map.items():
            if counter == 1:
                return value


        """

        map = {}
       

        for num in nums:
            if num in map:
                map[num] +=1
            else:
                map[num] = 1

        

        for value, counter in map.items():
            if counter == 1:
                return value
        return None
       



# this solution uses constant space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = i ^ res   
        return res
