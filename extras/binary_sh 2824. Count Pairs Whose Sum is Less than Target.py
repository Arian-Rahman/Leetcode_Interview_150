from typing import List
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        left ,right = 0 , len(nums)-1
        count=0
        nums.sort()
        while left<right:
            sum = nums[left]+nums[right]
            if sum<target:
                count+= right-left
                left+=1
            else :
                right-=1
        
        return count
        
def main():
    nums = [1, 3, 2, 4, 5]  # Example input
    target = 6  # Example target value
    solution = Solution()
    result = solution.countPairs(nums, target)
    print("Number of pairs:", result)

if __name__ == "__main__":
    main()
