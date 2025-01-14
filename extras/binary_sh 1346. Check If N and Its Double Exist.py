from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort() 
        for i in range(len(arr)):
            target = 2 * arr[i]  
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target and mid != i:  
                    return True
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False
