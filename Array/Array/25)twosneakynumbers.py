from typing import List
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen=set()
        dup=set()
        for num in nums:
            if num in seen:
                dup.add(num)
            else:
                seen.add(num)
        return list(dup)