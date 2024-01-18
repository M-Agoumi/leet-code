from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [freq[i][0] for i in range(k)]
    

nums = [1,1,1,2,2,3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))