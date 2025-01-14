from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = [0]* len(nums)
        prefix_sum[0] = nums[0]
        
        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1]+nums[i]
        
        indexs = []
        
        for q in queries:
            left,right = 0, len(prefix_sum)
            while left<right:
                mid = (left+right)//2
                if prefix_sum[mid] <= q :
                    left = mid+1
                else : 
                    right = mid
            indexs.append(left) # index of last satisfied value  

        return indexs
        



# class Solution:
#     def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
#         # Step 1: Sort the nums array
#         nums.sort()
        
#         # Step 2: Compute prefix sums for nums
#         prefix_sum = [0] * len(nums)
#         prefix_sum[0] = nums[0]
#         for i in range(1, len(nums)):
#             prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
#         # Step 3: For each query, use binary search to find the answer
#         result = []
#         for query in queries:
#             # Binary search to find the maximum size of subsequence with sum <= query
#             left, right = 0, len(prefix_sum)
#             while left < right:
#                 mid = (left + right) // 2
#                 if prefix_sum[mid] <= query:
#                     left = mid + 1
#                 else:
#                     right = mid
#             result.append(left)
        
#         return result


# Main function to execute the solution
if __name__ == "__main__":
    # Example input
    nums = [4, 5, 2, 1]
    queries = [3, 10, 21]
    
    # Initialize the solution class and call the method
    solution = Solution()
    result = solution.answerQueries(nums, queries)
    
    # Print the result
    print(result)  # Output should be the answer for each query
