class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        "{2:0,}"
        map ={}

        for index , value in enumerate(nums):
            diff = target - value
            if diff in map:
                return[ index, map[diff]]
            else:
                map[value] = index
        return []