from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
            
        min_sum = float('inf')
        
        for length in range(l, r + 1):
            for i in range(n - length + 1):
                subarray_sum = prefix[i + length] - prefix[i]
                if subarray_sum > 0:
                    min_sum = min(min_sum, subarray_sum)
    
        return min_sum if min_sum != float('inf') else -1


    
if __name__ == "__main__":
    solution = Solution()
    nums = [5,8,-6]
    l = 1  # Example left index
    r = 3  # Example right index
    print(solution.minimumSumSubarray(nums, l, r))  # Replace with actual function logic
