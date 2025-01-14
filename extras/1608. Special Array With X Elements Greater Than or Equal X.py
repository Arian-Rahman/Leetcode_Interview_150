from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True) 
        nums += [0] 
        for i in range(1, len(nums)):
            if nums[i - 1] >= i > nums[i]: 
                # check if i is greater than the next number but less than or equal to the current number
                return i 
        return -1 

# Main function to test the implementation
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([3, 5, 2, 7], 3),  # Example where x = 3
        ([0, 0], -1),        # No x can satisfy the condition
        ([0, 4, 3, 0, 4], 3),# Example where x = 3
        ([1, 2, 3, 4, 5], -1), # No valid x
        ([100, 200, 300], 3)   # Example where x = len(nums)
    ]
    
    # Execute test cases
    for nums, expected in test_cases:
        result = sol.specialArray(nums)
        print(f"nums: {nums} => Output: {result}, Expected: {expected}, Passed: {result == expected}")
