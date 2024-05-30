class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        if len(nums) < 2:
            return 0
        

        first = heapq.heappop(nums)
        second = heapq.heappop(nums)

        res = (first + 1) * (second + 1)
        
        return res