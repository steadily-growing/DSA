from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_nums={}
        for index, i in enumerate(nums):
            if target - i in final_nums.keys():
                return [final_nums[target-i], index]
            final_nums[i] = index