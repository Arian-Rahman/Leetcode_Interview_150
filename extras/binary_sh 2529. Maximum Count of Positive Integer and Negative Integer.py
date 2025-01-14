from bisect import bisect_left,bisect_right
from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = bisect_left(nums, 0)
        pos = len(nums) - bisect_right(nums, 0)
        return max(neg, pos)
    
class Solution:
    ## need to exclude 0 from positive side 
    
    def maximumCount(self, nums: List[int]) -> int:
        # Binary search to find the first zero or positive number
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < 0:  # Negative numbers
                left = mid + 1
            else:  # Zero or positive numbers
                right = mid

        # Now `left` is the count of strictly negative numbers
        neg_count = left

        # Binary search to find the first positive number
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= 0:  # Zeros or negatives
                left = mid + 1
            else:  # Positive numbers
                right = mid

        # Now `len(nums) - left` is the count of strictly positive numbers
        pos_count = len(nums) - left

        # Return the maximum of negatives or positives
        return max(neg_count, pos_count)

# Main function to execute the solution
if __name__ == "__main__":
    # Example input
    nums = [-2, -1, -1, 0,1, 1, 2, 3]
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the maximumCount function and store the result
    result = solution.maximumCount(nums)
    
    # Print the result
    print("Maximum count of positive or negative numbers:", result)