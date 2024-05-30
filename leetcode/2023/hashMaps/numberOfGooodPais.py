class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_pairs = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]==nums[j] and i<j:
                    count_pairs +=1
        return count_pairs