class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,count = 0,0

        for i in nums:
            if count == 0:
                res = i

            count +=(1 if i==res else -1)
        return res
    
    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        {3,2,3}
        {3:2, 2:1}
        return the index with the max value
        [3,2,3]

        boyer -moore --> O(1) space
        counter = 0
        res = 2
                 i
        [2,2,1,1,1,2,2]

        """
        counter, res = 0,0

        for num in nums:
            if counter == 0:
                res = num
                counter +=1
            elif num == res:
                counter +=1
            else:
                counter-=1
        return res