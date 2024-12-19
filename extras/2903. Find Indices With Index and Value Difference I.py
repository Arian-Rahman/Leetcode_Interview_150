from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        
        #if the array has less than 2 elements or indexDifference is too large
        if n == 0 or indexDifference >= n:
            return [-1, -1]
        
        for i in range(n):
            for j in range(i + indexDifference, n):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        
        return [-1, -1]
    
    
if __name__ == "__main__":

    solution = Solution()
    result = solution.findIndices(nums = [5,1,4,1], indexDifference = 2, valueDifference = 4)

    print(result )  