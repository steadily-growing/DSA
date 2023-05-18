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
            

