from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res =[1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

nums = [1,2,3,4] # Output: [24,12,8,6]
sol = Solution()
print(sol.productExceptSelf(nums))