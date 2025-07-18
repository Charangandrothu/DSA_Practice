from typing import List
class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        
        numset=set(nums)
        for num in range(1,10**5+2):
            if num not in numset:
                return num
            