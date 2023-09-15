class Solution:
    # Time complexity: O(n), Space complexity: O(1)
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        vid_count = [0]*60
        count = 0

        for duration in time:
            rem = duration%60
            if not rem:
                count += vid_count[0]
            else:
                count += vid_count[60-rem]
            vid_count[rem] += 1
        return count
      




