class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        candidate = None
        count = 0 
        for num in nums:
            if count == 0 :
                candidate = num
            count += (1 if candidate==num else -1 ) 

        return candidate





# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         middle = len(nums) //2
#         return  nums[middle]

        

        