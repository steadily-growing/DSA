class Solution:

    """
    First run - _veCount = 1, first_neg = 0, max_len =1 
    Second run - _veCount =2, first_neg = 0, max_len =2
    Third run - _veCount = 3, first_neg = 0, max_len =2
    Fourth ruun - _veCount = 0, first_neg = 0, max_len =
    Fifth run - _veCount = 0, first_neg = 0, max_len = 2

    Time & Space = O(n) & O(1)
    """
    def getMaxLen(self, nums: List[int]) -> int:
        start = 0
        end = 0
        negative_count = 0
        max_length = 0
        first_negative = -1 
        
        while end < len(nums):
            if nums[end] < 0:
                negative_count += 1
                if first_negative == -1:
                    first_negative = end
                    
            if nums[end] == 0:
                start = end + 1
                negative_count = 0
                first_negative = -1
            else:
                if negative_count % 2 == 0:
                    max_length = max(max_length, end - start + 1)
                else:
                    max_length = max(max_length, end - first_negative)
            
            end += 1
        return max_length