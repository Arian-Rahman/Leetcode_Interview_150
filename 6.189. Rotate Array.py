from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k= k%len(nums)
            
        nums[:] = nums[-k:] + nums[:-k]

# Main function to run the solution
if __name__ == "__main__":
    # Example input
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    
    # Print the original list
    print(f"Original list: {nums}")
    
    # Create a Solution object and call the rotate method
    solution = Solution()
    solution.rotate(nums, k)
    
    # Print the rotated list
    print(f"Rotated list: {nums}")
