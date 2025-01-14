from typing import List

# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         if len(nums)==1 :return nums[0]
#         n = len(nums)
#         result= [float("-inf")]*(n)
#         for i in range(n-k+1):
#             result[i] =  sum(nums[i:i+k])
#         maximum = max(result)/k
#         return maximum

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_avg = current_sum/k
        for i in range(k,len(nums)): # we don;t need to slide from i=1 becasue we handle/exclude it in the slide 
            current_sum += nums[i] - nums[i - k]
            max_avg = max(max_avg, current_sum / k)
        
        return max_avg


if __name__ == "__main__":
    nums = [0,1,1,3,3]
    k = 4
    solution = Solution()
    result = solution.findMaxAverage(nums, k)
    print(f"The maximum average subarray of length {k} is: {result}")
