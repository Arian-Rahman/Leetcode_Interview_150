from typing import List
from bisect import bisect_left

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = bisect_left(nums,target)
        
        if index<= len(nums) :
            return index

# Main function to test the solution
def main():
    solution = Solution()
    
    # Example test cases
    nums = [1, 3, 5, 6]
    target = 5
    print(solution.searchInsert(nums, target))  # Expected output: 2

    nums = [1, 3, 5, 6]
    target = 2
    print(solution.searchInsert(nums, target))  # Expected output: 1

    nums = [1, 3, 5, 6]
    target = 7
    print(solution.searchInsert(nums, target))  # Expected output: 4

    nums = [1, 3, 5, 6]
    target = 0
    print(solution.searchInsert(nums, target))  # Expected output: 0

if __name__ == "__main__":
    main()
