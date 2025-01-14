from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        p1,p2 = 0,0
        nums2.sort()
        nums1.sort()
        answer =[]
        while p1 < len(nums1) and p2<len(nums2):
            if nums1[p1] == nums2[p2] :
                answer.append(nums1[p1])
                p1+=1 
                p2+=1
            elif nums1[p1] > nums2[p2] :
                p2+=1
            else : 
                p1+=1
        return answer
        
    
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([1, 2, 2, 1], [2, 2]),      # Expected output: [2, 2]
        ([4, 9, 5], [9, 4, 9, 8, 4]), # Expected output: [4, 9] or [9, 4]
        ([1, 1, 1, 1], [1, 1]),       # Expected output: [1, 1]
        ([1, 2, 3], [4, 5, 6]),       # Expected output: []
    ]
    
    # Execute test cases
    for nums1, nums2 in test_cases:
        result = sol.intersect(nums1, nums2)
        print(f"nums1: {nums1}, nums2: {nums2} => Intersection: {result}")
