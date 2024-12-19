from typing import List

"""
Given a 0-indexed integer array nums of length n and an integer target, 
return the number of pairs (i, j) where 
0 <= i < j < n and 
nums[i] + nums[j] < target. 
"""
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        count = 0
        i,j = 0, len(nums)-1
        nums.sort()
        while i<j:
            sum = nums[i]+nums[j]  
            if sum < target:
                i-=1
                count+=(j-i)
            else :
                j-=1            
        return count

def main():
    solution_instance = Solution()
    result = solution_instance.countPairs(nums=[-1,1,2,3,1], target = 2) # -1,1,1,2,3
    print(result)

if __name__ == "__main__":
    main()
