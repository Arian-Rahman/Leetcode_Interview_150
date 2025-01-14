from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums.sort()
        
        min_diff = float('inf')
        
        for i in range(len(nums) - k + 1):
            # The difference between the first and last elements in the window
            diff = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, diff)
        
        return min_diff
