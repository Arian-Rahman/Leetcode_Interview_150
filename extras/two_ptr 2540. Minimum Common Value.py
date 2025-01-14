from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
               return nums1[i]
            elif nums1[i] >=nums2[j]:
                j+=1
            else : i+=1
            
        return -1
        


# Main function to execute the code
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([1, 2, 3, 4], [3, 4, 5, 6]),  # Common element is 3
        ([1, 3, 8], [2, 3, 5]),        # Common element is 3
        ([1, 2, 3], [4, 5, 6]),        # No common element
        ([7, 8, 9], [9, 10, 11]),      # Common element is 9
    ]
    
    # Execute test cases
    for nums1, nums2 in test_cases:
        result = sol.getCommon(nums1, nums2)
        print(f"nums1: {nums1}, nums2: {nums2} => Common element: {result}")
