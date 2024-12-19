from typing import List

"""
Given a 0-indexed integer array nums of length n and an integer target, 
return the number of pairs (i, j) where 
0 <= i < j < n and 
nums[i] + nums[j] < target. 
"""
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        count = 0     
        return count

def main():
    solution_instance = Solution()
    result = solution_instance.pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10)
    print(result)

if __name__ == "__main__":
    main()
