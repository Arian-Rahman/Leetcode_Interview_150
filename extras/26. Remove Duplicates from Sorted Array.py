from typing import List
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i,j=0,1
#         while j<len(nums) and i<len(nums)-1:
#             while nums[i]==nums[j]:
#                 nums[j] = "_"
#                 #print(nums)
#                 if j< len(nums)-1 :j+=1   # check array index limit before increment
#                 else : break      
#             print(nums)
            
#             nums[i+1] = nums[j]
#             i+=1
#         return nums

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0  
        for j in range(1, len(nums)):  
            if nums[i] != nums[j]:  
                i += 1  
                nums[i] = nums[j]  
                print(nums)
        
        return i + 1 
            
                
        
    
if __name__=="__main__":
    nums = [1,1,1,2,4,4,5,5,5,3,4,4,4,4]
    
    s = Solution()
    result = s.removeDuplicates(nums=nums)
    print(result)