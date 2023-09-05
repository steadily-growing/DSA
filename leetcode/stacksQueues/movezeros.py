class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0
        r = 0
      
        while r < (len(nums)):
            if nums[r] == 0:
                r+=1
            else:
                nums[l], nums[r]= nums[r], nums[l]
                l+=1
                r+=1
                
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
           l
               r
        [1,0,0,4,6]
           l
           r
        [0,1,0,4,6]
        """
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1       
