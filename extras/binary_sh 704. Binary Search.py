from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right=mid-1 
            else :
                left =mid+1
        
        return -1

# Main function to test the implementation
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([5],5),
        ([-1,0,3,5,9,12],9),
        ([1, 2, 3, 4, 5], 3),  # Target exists in the list
        ([10, 20, 30, 40, 50], 25), # Target does not exist in the list
        ([5, 7, 9, 11], 7),  # Target exists in the list
        ([1, 3, 5, 7], 6),  # Target does not exist in the list
        ([1, 2, 3, 4], 1)   # Target exists as the first element
    ]
    
    # Execute test cases
    for nums, target in test_cases:
        result = sol.search(nums, target)
        print(f"nums: {nums}, target: {target} => Output: {result}")
