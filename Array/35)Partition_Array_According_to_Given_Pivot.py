from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [0] * n  
        left, right = 0, n - 1
        for num in nums:
            if num < pivot:
                res[left] = num
                left += 1
        for num in reversed(nums):
            if num > pivot:
                res[right] = num
                right -= 1
        for num in nums:
            if num == pivot:
                res[left] = num
                left += 1
        return res    
