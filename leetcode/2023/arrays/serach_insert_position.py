#first attempt this is not ologn 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == target:
               return i
            elif nums[i] < target:
                i +=1
        return i 
            
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """

             l
        [1,3,5,6]
           l
        [1,3,5,6]
        """
        i = 0

        while i < len(nums):
            if nums[i] >= target:
                return i
            else:
                i+=1
        return i
        

