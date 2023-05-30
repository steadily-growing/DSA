class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        container = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                container.remove(nums[L])
                L+=1
            if nums[R] in container:
                return True
            container.add(nums[R])
        return False