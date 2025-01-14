from typing import List
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        
        return result

    

def main():
    solution = Solution()
    
    nums = [1,2,5,2,3]
    target = 2
    # Call the targetIndices method
    result = solution.targetIndices(nums, target)
    
    # Print the result
    print("Target indices:", result)

# Call the main function
if __name__ == "__main__":
    main()

