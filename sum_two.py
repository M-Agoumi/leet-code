from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in num_index:
                return [num_index[complement], idx]
            num_index[num] = idx

sol = Solution()
nums = [3,3]
target = 6
print(sol.twoSum(nums, target))
