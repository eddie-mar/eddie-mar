from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tested = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in tested:
                return [tested[complement], i]
            tested[num] = i
        return []
    