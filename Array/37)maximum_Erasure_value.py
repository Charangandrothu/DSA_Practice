from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        sum = 0
        max_sum = 0
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                sum -= nums[left]
                left += 1
            seen.add(nums[right])
            sum += nums[right]
            max_sum = max(max_sum, sum)
        return max_sum