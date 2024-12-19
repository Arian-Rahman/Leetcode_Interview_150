from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        # flattened = [element for row in matrix for element in row]
        # print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        new_list = nums1+nums2
        sum_values ={}
        for row in new_list:
            index,value = row # row = [2,4] for example 
            if index in sum_values:
                sum_values[index]+=value
            else :
                sum_values[index] = value

        answer = [[index,value] for index,value in sorted(sum_values.items()) ]
        return answer
    
        
if __name__ == "__main__":
    nums1 = [[1, 2], [2, 3], [4, 5],[7,6]]  
    nums2 = [[1, 4], [3, 2], [4, 1]]  
    
    solution = Solution()
    result = solution.mergeArrays(nums1, nums2)
    print(result)  
