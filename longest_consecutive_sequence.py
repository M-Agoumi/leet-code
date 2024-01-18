from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Check if the current number is the start of a streak
            if num - 1 not in num_set:
                length = 0
                # Extend the streak as far as possible
                while num + length in num_set:
                    length += 1
                # Update the longest streak
                longest_streak = max(longest_streak, length)

        return longest_streak


nums = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums)) # Output: 9