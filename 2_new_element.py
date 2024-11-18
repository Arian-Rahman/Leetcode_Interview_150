from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None:
            return 0
        for num in nums : 
            if num == val:
                nums.remove(num)
            
        return len(nums)

def main():
    nums = [3, 2, 2, 3]
    val = 3
    
    solution = Solution()
    
    result = solution.removeElement(nums, val)
    
    print("New length:", result)
    print("Modified array:", nums[:result])  

if __name__ == "__main__":
    main()
