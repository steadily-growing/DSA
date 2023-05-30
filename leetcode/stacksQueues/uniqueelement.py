class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashset = set()
        unique_set = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                if nums[i] in unique_set:
                    unique_set.remove(nums[i]) 
            else:
                hashset.add(nums[i])
                unique_set.add(nums[i])
        return sum(unique_set)


