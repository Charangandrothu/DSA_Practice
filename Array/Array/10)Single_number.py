from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            result=result^num
        return result