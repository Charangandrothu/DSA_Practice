from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        total=n*(n+1)//2
        return total-sum(nums)