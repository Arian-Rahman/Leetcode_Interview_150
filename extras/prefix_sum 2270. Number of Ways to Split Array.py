from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  
        prefix_sum = 0
        counter = 0
        
        # Iterate through the array (excluding the last element to avoid empty right part)
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]  
            right_sum = total_sum - prefix_sum  
            
            if prefix_sum >= right_sum: 
                counter += 1
        
        return counter

               

def main():
    # Example input
    nums = [10, 4, -8, 7]
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the waysToSplitArray method and print the result
    result = solution.waysToSplitArray(nums)
    print("Result:", result)

if __name__ == "__main__":
    main()
