class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
    
## second try i used two pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """"
        l  r
        [1,1,2]

         l        r  
        [1,2]

        l  r
        [0,0,1,1,1,2,2,3,3,4]
           l r
        [0,1,1,1,2,2,3,3,4]


        """
        l = 0
        r = l+1

        while r < len(nums):
            if nums[l] == nums[r]:
               del(nums[r])
            else:
                l+=1
                r = l+1
               
        return len(nums)
       
