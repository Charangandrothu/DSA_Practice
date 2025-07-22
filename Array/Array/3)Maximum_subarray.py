from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=maxSubArray=nums[0]
        for num in nums[1:]:
            current_sum=max(num,current_sum+num)
            maxSubArray=max(maxSubArray,current_sum)
        return maxSubArray